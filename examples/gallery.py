"""Reproducible gallery of synthetic plots using mplume's public API.

Run: python examples/gallery.py --output examples/output
All signals are generated in memory; no experimental data is included.
"""
import argparse
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import mplume as mp


def generate(output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    x = np.linspace(-3.0, 3.0, 800)

    # 01: Zoom inset on a synthetic asymmetric peak.
    with mp.style("box", "paper"):
        fig, ax = mp.figure("single")
        y = np.exp(-x*x) + 0.08*np.exp(-60*(x-0.4)**2)
        ax.plot(x, y, label="Synthetic signal")
        ax.set(xlabel="Position (a.u.)", ylabel="Intensity (a.u.)")
        mp.zoom(ax, xlim=(0.1, 0.8), ylim=(0.6, 1.1), loc="upper left")
        fig.savefig(output / "01-zoom.svg", bbox_inches="tight")
        plt.close(fig)

    # 02: Non-destructive waterfall / stacked intensity curves.
    with mp.style("box", "paper"):
        curves = np.array([np.exp(-((x-d)/0.42)**2) for d in (-0.45, -0.1, 0.25, 0.6)])
        original = curves.copy()
        fig, ax = mp.figure("single")
        mp.stack(ax, x, curves, spacing=1.25,
                 labels=["A", "B", "C", "D"])
        assert np.array_equal(curves, original), "stack modified input"
        ax.set(xlabel="Position (a.u.)", ylabel="Offset intensity (a.u.)")
        ax.legend(loc="upper right")
        fig.savefig(output / "02-stack.svg", bbox_inches="tight")
        plt.close(fig)

    # 03: Common two-panel composition with ordinary Matplotlib.
    with mp.style("house", "paper"):
        fig, axes = mp.subplots("double", ncols=2)
        axes[0].plot(x, np.exp(-x*x))
        axes[0].set(xlabel="Position (a.u.)", ylabel="Amplitude")
        mp.panel_label(axes[0], "a")
        axes[1].plot(x, np.exp(-x*x) ** 2)
        axes[1].set(xlabel="Position (a.u.)", ylabel="Intensity")
        mp.panel_label(axes[1], "b")
        fig.tight_layout()
        fig.savefig(output / "03-panels.svg", bbox_inches="tight")
        plt.close(fig)
    return [output / name for name in ("01-zoom.svg", "02-stack.svg", "03-panels.svg")]


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", default="examples/output", type=Path)
    args = p.parse_args()
    for path in generate(args.output):
        print(path)
