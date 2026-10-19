"""Reproduce the numerical evidence and figures of chapter 11."""

import argparse
import hashlib
import io
import json
import math
import platform
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd


def summarize(values):
    values = np.asarray(values, dtype=float)
    return {"n": len(values), "mean": float(values.mean()),
            "median": float(np.median(values)), "rmse": float(np.sqrt(np.mean(values**2))),
            "p95": float(np.percentile(values, 95)), "maximum": float(values.max())}


def git_blob_sha(content):
    header = f"blob {len(content)}\0".encode()
    return hashlib.sha1(header + content).hexdigest()


def save_pdf(fig, path):
    buffer = io.BytesIO()
    fig.savefig(buffer, format="pdf", bbox_inches="tight")
    path.write_bytes(buffer.getvalue())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--system-root", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    data = root / "data/chapter11"
    output = root / "figures/chapter11"
    output.mkdir(parents=True, exist_ok=True)
    provenance = json.loads((data / "provenance.json").read_text(encoding="utf-8"))
    for name, details in provenance["inputs"].items():
        if hashlib.sha256((data / name).read_bytes()).hexdigest() != details["sha256"]:
            raise ValueError(f"Experimental input differs from the documented source: {name}")
    source_hashes = {}
    for name, details in provenance["system_files"].items():
        content = (args.system_root / name).read_bytes()
        if git_blob_sha(content) != details["github_blob_sha"]:
            raise ValueError(f"System source differs from the documented version: {name}")
        source_hashes[name] = hashlib.sha256(content).hexdigest()
    sys.path.insert(0, str(args.system_root.resolve()))
    from Utils.Cls.TrackInspector import TrackInspector
    from Utils.Cls.MovementClassifier import MovementClassifier
    from Utils.Move import compute_acceleration
    from Utils.Speed import get_track_speeds_and_frames
    from Utils.Temporal import detect_gaps

    fps = 30.0
    window = 20
    raw_ref = json.loads((data / "ground_truth.json").read_text(encoding="utf-8"))
    ref = pd.DataFrame(raw_ref["tracks"]["1"], columns=["frame", "x_manual", "y_manual"])
    pred = pd.read_csv(data / "Track_145.csv")
    for frame in (ref, pred):
        assert frame.frame.is_unique and np.isfinite(frame.to_numpy()).all()
        assert np.equal(frame.frame, np.round(frame.frame)).all()
        frame["frame"] = frame.frame.astype(int)
        assert np.all(np.diff(frame.frame) > 0)
    common = ref.merge(pred, on="frame", validate="one_to_one").sort_values("frame")
    first = common.iloc[0]
    assert int(first.frame) == 0
    offset = float(first.y_manual + first.y_px)
    ref["y_aligned"] = offset-ref.y_manual
    common["y_aligned"] = offset-common.y_manual
    common["error_px"] = np.hypot(common.x_px-common.x_manual, common.y_px-common.y_aligned)
    common["raw_error_px"] = np.hypot(common.x_px-common.x_manual, common.y_px-common.y_manual)
    common["anchor"] = common.frame == 0
    evaluated = common.loc[~common.anchor]
    assert len(common) == 93 and len(evaluated) == 92
    common.to_csv(data / "position_comparison.csv", index=False)

    points = [(int(r.frame), float(r.x_px), float(r.y_px)) for r in pred.itertuples()]
    inspector = TrackInspector({145: points}, 145, analysis_fps=fps)
    info = inspector.get_info(window_size=window, vel_min=30.0)
    speeds = np.asarray(inspector.get_speeds())
    smooth = np.asarray(inspector.get_smoothed_speeds(window))
    speed_frames = np.asarray(inspector.get_frames())
    smooth_frames = np.asarray(inspector.get_smoothed_frames(window))
    frames = pred.frame.to_numpy()
    gaps = detect_gaps(frames.tolist())
    acceleration = compute_acceleration(smooth, smooth_frames, fps)
    independent_distance = np.array([math.dist(a[1:], b[1:]) for a,b in zip(points, points[1:])])
    independent_speed = independent_distance/(np.diff(frames)/fps)
    independent_smooth = np.array([sum(independent_speed[i:i+window])/window
                                   for i in range(len(independent_speed)-window+1)])
    np.testing.assert_allclose(speeds, independent_speed, rtol=1e-12, atol=1e-10)
    np.testing.assert_allclose(smooth, independent_smooth, rtol=1e-12, atol=1e-10)
    np.testing.assert_allclose(acceleration, np.diff(independent_smooth)/(np.diff(smooth_frames)/fps),
                               rtol=1e-10, atol=1e-8)
    assert abs(sum(independent_distance)-info["total_distance_px"]) < 0.000051
    assert int((smooth < 30).sum()) == len(info["inactivity_frames"])
    pd.DataFrame({"start_frame": frames[:-1], "end_frame": frames[1:],
                  "delta_t_s": np.diff(frames)/fps, "speed_px_s": speeds}).to_csv(data / "speed_segments.csv", index=False)
    pd.DataFrame({"frame": smooth_frames, "time_s": smooth_frames/fps,
                  "speed_px_s": smooth, "inactive": smooth < 30}).to_csv(data / "speed_smoothed.csv", index=False)

    rp = [(int(r.frame), float(r.x_manual), float(r.y_aligned)) for r in common.itertuples()]
    pp = [(int(r.frame), float(r.x_px), float(r.y_px)) for r in common.itertuples()]
    manual_v, _ = get_track_speeds_and_frames({1: rp}, 1, analysis_fps=fps)
    model_v, _ = get_track_speeds_and_frames({1: pp}, 1, analysis_fps=fps)
    v_error = np.asarray(model_v)-manual_v
    pd.DataFrame({"start_frame": common.frame.to_numpy()[:-1], "end_frame": common.frame.to_numpy()[1:],
                  "manual_speed_px_s": manual_v, "model_speed_px_s": model_v,
                  "difference_px_s": v_error}).to_csv(data / "speed_comparison.csv", index=False)
    classifier_results = {
        "model_full": inspector.classify_movement(),
        "model_common_frames": MovementClassifier(pp, analysis_fps=fps).classify(),
        "manual_common_frames": MovementClassifier(rp, analysis_fps=fps).classify(),
    }

    training = {}
    columns = ["metrics/precision(B)", "metrics/recall(B)", "metrics/mAP50(B)", "metrics/mAP50-95(B)"]
    for version in ("v1", "v2"):
        t = pd.read_csv(data / f"entrenamiento_{version}.csv")
        t.columns = t.columns.str.strip()
        assert len(t) == 100 and np.isfinite(t[columns]).all().all()
        best = t.loc[t[columns[-1]].idxmax()]
        training[version] = {"curve": t,
            "individual_maxima": {col: {"value": float(t[col].max()), "epoch": int(t.loc[t[col].idxmax(), "epoch"])} for col in columns},
            "row_at_maximum_map50_95": {col: float(best[col]) for col in ["epoch"]+columns},
            "epochs_with_nan_validation_loss": int(t[["val/box_loss", "val/cls_loss", "val/dfl_loss"]].isna().any(axis=1).sum())}
    regime_indices = [i for i in range(50, len(smooth)-50)
                       if abs(np.mean(smooth[i:i+50])-np.mean(smooth[i-50:i])) >= 30]
    summary = {
        "alignment": {"equation": "y_aligned = offset - y_manual; x unchanged", "offset": offset, "anchor_frame": 0, "scale": 1.0},
        "position_after_anchor": summarize(evaluated.error_px),
        "position_raw_after_anchor": summarize(evaluated.raw_error_px),
        "position_counts": {"reference": len(ref), "predicted": len(pred), "common": len(common),
                            "evaluated": len(evaluated), "within_10_px": int((evaluated.error_px <= 10).sum()),
                            "missing_reference_frames": sorted(set(ref.frame)-set(pred.frame))},
        "track_info": info, "gaps": gaps,
        "missing_frames_within_track": sum(b-a-1 for a,b in gaps),
        "smoothed_speed_range": [float(smooth.min()), float(smooth.max())],
        "inactivity": {"sample_count": len(smooth), "inactive_samples": int((smooth < 30).sum())},
        "acceleration": {"minimum": float(acceleration.min()), "maximum": float(acceleration.max()),
                         "samples_above_450": int((acceleration > 450).sum()),
                         "samples_below_minus_450": int((acceleration < -450).sum())},
        "regime_marked_samples": len(regime_indices),
        "speed_comparison": {"interval_count": len(v_error), "mae": float(np.abs(v_error).mean()),
                             "rmse": float(np.sqrt(np.mean(v_error**2))), "correlation": float(np.corrcoef(manual_v, model_v)[0,1])},
        "classification": classifier_results,
        "training": {k: {p: v for p,v in row.items() if p != "curve"} for k,row in training.items()},
        "source_sha256": source_hashes,
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "pandas": pd.__version__, "matplotlib": matplotlib.__version__},
        "independent_calculation_check": "passed: segment speed, total distance, moving average, inactivity and acceleration",
    }
    (data / "results.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.titlesize": 9,
                         "axes.spines.top": False, "axes.spines.right": False, "pdf.fonttype": 42})
    decimal = FuncFormatter(lambda value, _: f"{value:g}".replace(".", ","))
    fig, axes = plt.subplots(1, 2, figsize=(6.3, 2.75), layout="constrained")
    for ax, metric, title in zip(axes, columns[-2:], ["A. mAP@0,50", "B. mAP@0,50:0,95"]):
        for v, style in [("v1", "-"), ("v2", "--")]:
            curve = training[v]["curve"]
            ax.plot(curve.epoch, curve[metric], style, lw=1, label=f"Versión {v[-1]}")
        ax.set(title=title, xlabel="Época", ylim=(0, 1.03), xlim=(1, 100))
        ax.yaxis.set_major_formatter(decimal)
        ax.grid(alpha=.2)
        ax.legend(fontsize=8, loc="lower right")
    save_pdf(fig, output / "fig11_01_metricas_detector.pdf")
    plt.close(fig)

    fig, (xy_ax, e_ax) = plt.subplots(1, 2, figsize=(6.3, 4.4), layout="constrained", width_ratios=(1, 1.15))
    for i, (_, block) in enumerate(pred.groupby((pred.frame.diff().fillna(1) > 1).cumsum())):
        xy_ax.plot(block.x_px, block.y_px, color="0.3", lw=1, label="Modelo" if i == 0 else None)
    xy_ax.scatter(ref.x_manual, ref.y_aligned, s=9, facecolors="none", edgecolors="#17618a", lw=.7, label="Tracker alineado")
    xy_ax.scatter([first.x_px], [first.y_px], marker="*", s=40, color="#9b5100", label="Anclaje")
    xy_ax.set(title="A. Trayectorias", xlabel="X (px)", ylabel="Y de imagen (px)")
    xy_ax.set_aspect("equal", adjustable="box")
    xy_ax.invert_yaxis()
    xy_ax.legend(loc="upper left", fontsize=6.5)
    xy_ax.grid(alpha=.2)
    e_ax.scatter(evaluated.frame/fps, evaluated.error_px, color="#17618a", s=11)
    e_ax.axhline(evaluated.error_px.mean(), ls="--", color="0.4", lw=.9, label="Media: 5,33 px")
    e_ax.set(title="B. Discrepancia posterior", xlabel="Tiempo del video (s)", ylabel="Error de posición (px)", ylim=(0, 16.5))
    e_ax.grid(alpha=.2)
    e_ax.legend(loc="upper right", fontsize=7)
    save_pdf(fig, output / "fig11_02_comparacion_trayectorias.pdf")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.3, 2.9), layout="constrained")
    for s, e in gaps:
        ax.axvspan(s/fps, e/fps, color="0.9", zorder=0)
    def broken_plot(vframes, values, **kwargs):
        xs, ys = [], []
        for i, (frame, value) in enumerate(zip(vframes, values)):
            if i and frame-vframes[i-1] > 1:
                xs.append(np.nan); ys.append(np.nan)
            xs.append(frame/fps); ys.append(value)
        ax.plot(xs, ys, **kwargs)
    broken_plot(speed_frames, speeds, color="0.65", lw=.55, label="Por segmento")
    broken_plot(smooth_frames, smooth, color="#17618a", lw=1, label="Media móvil (20 muestras)")
    ax.axhline(30, color="0.2", ls="--", lw=.8, label="Umbral: 30 px/s")
    ax.set(xlabel="Tiempo del video (s)", ylabel="Rapidez (px/s)", xlim=(0, 34), ylim=(0, 430))
    ax.legend(loc="upper right", fontsize=7)
    ax.grid(alpha=.15)
    save_pdf(fig, output / "fig11_03_rapidez.pdf")
    plt.close(fig)
    print(json.dumps({"position_mean_px": summary["position_after_anchor"]["mean"],
                      "speed_comparison": summary["speed_comparison"], "classification": classifier_results["model_full"]["movement_type"],
                      "checks": "passed", "figures": 3}, ensure_ascii=False))


if __name__ == "__main__":
    main()
