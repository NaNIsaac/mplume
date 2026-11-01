"""Create synthetic mplume zoom and stack examples."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import mplume as mp

out = Path("examples/output")
out.mkdir(parents=True, exist_ok=True)
x = np.linspace(-3, 3, 800)
y = np.exp(-x*x) + 0.08 * np.exp(-60*(x-0.4)**2)
with mp.style("box", "paper"):
    fig, ax = mp.figure("single")
    ax.plot(x, y)
    ax.set(xlabel="Position", ylabel="Intensity (a.u.)")
    mp.zoom(ax, (0.1, 0.8), (0.6, 1.1))
    fig.savefig(out / "zoom.png", dpi=180)
    plt.close(fig)

    curves = np.array([np.exp(-((x-d)/0.5)**2) for d in (-0.3, 0, 0.3)])
    fig, ax = mp.figure("single")
    mp.stack(ax, x, curves, spacing=1.15, labels=["A", "B", "C"])
    ax.legend()
    ax.set(xlabel="Position", ylabel="Offset intensity")
    fig.savefig(out / "stack.png", dpi=180)
    plt.close(fig)
