"""Reproduce the distance and straightness example from the saved Track_145 data."""

import hashlib
import io
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd


def decimal(value, digits=2):
    return f"{value:.{digits}f}".replace(".", "{,}")


def main():
    root = Path(__file__).resolve().parents[1]
    source = root / "data/chapter11/Track_145.csv"
    provenance = json.loads((source.parent / "provenance.json").read_text())
    source_sha = hashlib.sha256(source.read_bytes()).hexdigest()
    assert source_sha == provenance["inputs"][source.name]["sha256"]
    track = pd.read_csv(source)
    frames = track.frame.to_numpy()
    xy = track[["x_px", "y_px"]].to_numpy()
    assert len(track) == 929 and np.isfinite(xy).all()
    assert np.all(np.diff(frames) > 0)
    segment_lengths = np.linalg.norm(np.diff(xy, axis=0), axis=1)
    total = float(segment_lengths.sum())
    net = float(np.linalg.norm(xy[-1] - xy[0]))
    straightness = net / total
    gap_segments = np.flatnonzero(np.diff(frames) > 1)
    saved = json.loads((source.parent / "results.json").read_text())["track_info"]
    assert abs(total - saved["total_distance_px"]) < 0.000051

    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 9,
        "axes.spines.top": False, "axes.spines.right": False,
        "pdf.fonttype": 42,
    })
    fig, (ax, key) = plt.subplots(
        1, 2, figsize=(6.1, 3.5), layout="constrained",
        gridspec_kw={"width_ratios": [1.25, 1]},
    )
    # Straight connections across gaps contribute to D_T but remain visually distinct.
    blocks = np.split(np.arange(len(track)), gap_segments + 1)
    for block in blocks:
        ax.plot(xy[block, 0], xy[block, 1], color="0.1", lw=1.2)
    for index in gap_segments:
        ax.plot(xy[index:index + 2, 0], xy[index:index + 2, 1],
                color="0.4", lw=1.1, ls=":")
    ax.plot(xy[[0, -1], 0], xy[[0, -1], 1], color="0.5", lw=1.2, ls="--")
    ax.scatter(*xy[0], marker="o", s=37, facecolor="white", edgecolor="black", zorder=4)
    ax.scatter(*xy[-1], marker="s", s=30, facecolor="black", edgecolor="black", zorder=4)
    ax.annotate("Inicio", xy[0], xytext=(8, 0), textcoords="offset points", va="center")
    ax.annotate("Fin", xy[-1], xytext=(-9, -1), textcoords="offset points",
                ha="right", va="center")
    ax.set(xlabel="X (px)", ylabel="Y de imagen (px)")
    ax.set_aspect("equal", adjustable="box")
    ax.margins(x=0.12, y=0.09)
    ax.invert_yaxis()
    ax.grid(alpha=0.2, lw=0.6)

    key.axis("off")
    key.text(0, 0.96, "Track 145", transform=key.transAxes,
             fontsize=11, fontweight="bold", va="top")
    handles = [
        Line2D([], [], color="0.1", lw=1.2, label="Recorrido observado"),
        Line2D([], [], color="0.4", lw=1.1, ls=":", label="Conexiones ante gaps"),
        Line2D([], [], color="0.5", lw=1.2, ls="--", label="Desplazamiento neto"),
    ]
    key.legend(handles=handles, loc="upper left", bbox_to_anchor=(-0.035, 0.86),
               frameon=False, borderaxespad=0, fontsize=8.5, handlelength=2.6,
               labelspacing=0.8)
    key.text(0, 0.50,
             "Distancia acumulada\n" + rf"$D_T = {decimal(total)}$ px" + "\n\n"
             "Distancia entre extremos\n" + rf"$D_N = {decimal(net)}$ px" + "\n\n"
             "Índice de rectitud\n" + rf"$S = D_N/D_T = {decimal(straightness, 4)}$",
             transform=key.transAxes, va="top", linespacing=1.45)

    output = root / "figures/chapter08/fig08_01_distancias_trayectoria.pdf"
    output.parent.mkdir(parents=True, exist_ok=True)
    buffer = io.BytesIO()
    fig.savefig(buffer, format="pdf", bbox_inches="tight")
    output.write_bytes(buffer.getvalue())
    plt.close(fig)

    details = {
        "source_csv": str(source.relative_to(root)), "source_sha256": source_sha,
        "source_url": provenance["inputs"][source.name]["url"],
        "original_trajectory_image_url": "https://drive.google.com/file/d/19CvMjL0DK5pJ4kehpPFECGC593ext034/view",
        "observations": len(track), "first_frame": int(frames[0]),
        "last_frame": int(frames[-1]), "start_xy_px": xy[0].tolist(),
        "end_xy_px": xy[-1].tolist(), "total_distance_px": total,
        "net_distance_px": net, "straightness": straightness,
        "gap_connections": [[int(frames[i]), int(frames[i + 1])] for i in gap_segments],
        "distance_rule": "Sum Euclidean distances over every consecutive pair of saved observations, including gaps.",
        "plot_rule": "Equal spatial scale in X and Y; inverted image Y; dotted connections across gaps; dashed endpoint displacement; no interpolation or smoothing.",
    }
    record = root / "data/chapter08/fig08_01_distancias_trayectoria.json"
    record.parent.mkdir(parents=True, exist_ok=True)
    record.write_text(json.dumps(details, indent=2, ensure_ascii=False) + "\n")
    print(f"D_T={total:.4f} px; D_N={net:.4f} px; S={straightness:.4f}")


if __name__ == "__main__":
    main()
