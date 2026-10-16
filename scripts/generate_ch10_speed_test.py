"""Generate the controlled speed test in chapter 10 from the system functions."""

import argparse
import hashlib
import json
import platform
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--system-root", type=Path, required=True)
    parser.add_argument("--system-version", required=True)
    parser.add_argument("--output-dir", type=Path,
                        default=Path(__file__).resolve().parents[1] / "figures/chapter10")
    args = parser.parse_args()
    system_root = args.system_root.resolve()
    sys.path.insert(0, str(system_root))
    from Utils.Speed import get_track_speeds_and_frames

    points = [(0, 0.0, 0.0), (1, 2.0, 0.0), (4, 8.0, 0.0), (5, 10.0, 0.0)]
    fps = 30.0
    expected = np.array([60.0, 60.0, 60.0])
    calculated, end_frames = get_track_speeds_and_frames({1: points}, 1, analysis_fps=fps)
    np.testing.assert_allclose(calculated, expected, rtol=1e-12, atol=1e-12)
    assert end_frames == [1, 4, 5]

    args.output_dir.mkdir(parents=True, exist_ok=True)
    stem = args.output_dir / "fig10_01_prueba_rapidez_gaps"
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "pdf.fonttype": 42})
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.3, 2.8), layout="constrained")
    times = np.array([p[0] for p in points]) / fps
    xs = [p[1] for p in points]
    ax1.axvspan(1.5 / fps, 3.5 / fps, color="0.9", label="Cuadros 2 y 3 ausentes")
    ax1.plot(times, xs, "ko", ms=4, label="Posiciones registradas")
    for frame, t, x in zip([p[0] for p in points], times, xs):
        ax1.annotate(f"f={frame}", (t, x), xytext=(0, 7),
                     textcoords="offset points", ha="center", fontsize=8)
    ax1.set(xlabel="Tiempo del video (s)", ylabel="Posición X (px)",
            title="A. Observaciones de entrada", ylim=(-1, 12.5), xlim=(-0.012, 0.18))
    ax1.set_xticks([0, 0.05, 0.10, 0.15], ["0", "0,05", "0,10", "0,15"])
    ax1.set_yticks([0, 5, 10])
    ax1.legend(loc="upper left", bbox_to_anchor=(0, -0.27), fontsize=7.5, frameon=False)
    ax2.axhline(60, color="0.45", ls="--", lw=1, label="Valor esperado: 60 px/s")
    ax2.plot(range(3), calculated, "ko", ms=5, label="Resultado del sistema")
    ax2.set_xticks(range(3), ["0 → 1", "1 → 4", "4 → 5"])
    ax2.set(xlabel="Segmento (cuadros)", ylabel="Rapidez por segmento (px/s)",
            title="B. Resultado y referencia", ylim=(0, 75), xlim=(-0.5, 2.5))
    ax2.legend(loc="upper left", bbox_to_anchor=(0, -0.27), fontsize=7.5, frameon=False)
    fig.savefig(stem.with_suffix(".pdf"), bbox_inches="tight")
    plt.close(fig)
    report = {
        "system_version": args.system_version,
        "function": "Utils.Speed.get_track_speeds_and_frames",
        "source_sha256": {
            path: hashlib.sha256((system_root / path).read_bytes()).hexdigest()
            for path in ("Utils/Speed.py", "Utils/Temporal.py", "Utils/Constants.py")
        },
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "matplotlib": matplotlib.__version__},
        "analysis_fps": fps,
        "points": points,
        "segment_end_frames": end_frames,
        "expected_speed_px_s": expected.tolist(),
        "calculated_speed_px_s": [float(v) for v in calculated],
        "absolute_error_px_s": np.abs(np.asarray(calculated) - expected).tolist(),
        "assertion": {"rtol": 1e-12, "atol": 1e-12, "passed": True},
    }
    stem.with_suffix(".json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                                         encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
