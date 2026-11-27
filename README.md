# mplume

Publication-ready scientific styles and figure composition for Matplotlib.

Traditional scientific graphs with inward major/minor ticks, closed frames,
grid-free presentation, paper/slide/poster typography, and helpers for
zoom insets and vertically stacked curves.

## Install

pip install mplume

Version 0.2.0 is available on PyPI and includes `zoom` and `stack`.

## Quick start

    import numpy as np
    import matplotlib.pyplot as plt
    import mplume as mp

    x = np.linspace(-3, 3, 600)
    y = np.exp(-x*x) + 0.08*np.exp(-60*(x-0.4)**2)
    with mp.style("box", "paper"):
        fig, ax = mp.figure("single")
        ax.plot(x, y)
        mp.zoom(ax, xlim=(0.1, 0.8), ylim=(0.6, 1.1))
        fig.savefig("figure.pdf")

## Core API

- mp.use("box", "paper") applies rcParams globally.
- with mp.style("box", "paper") temporarily sets plotting defaults.
- box is a classic four-sided scientific frame with inward major/minor ticks.
- house is a lighter two-sided style.
- paper, slide, poster, a0 select typography scale; a0 is for figures drawn at print size on an A0 poster.
- mp.figure("single") and mp.subplots("double", ncols=2) select figure width.
- mp.panel_label(ax, "a") labels an axes panel.
- mp.zoom(ax, xlim, ylim) creates a linked zoom inset.
- mp.stack(ax, x, ys, spacing="auto") adds display-only vertical offsets.

See the [reproducible figure gallery](docs/gallery.md) for zoom, stacked traces and two-panel figures.

## Documentation

- [Figure gallery](docs/gallery.md) — zoom, stacked traces and two-panel figures, each with its script
- [Composition notes](docs/composition.md) — what the zoom helper copies and where stack offsets live, with the limitations
- [examples/scientific.py](examples/scientific.py) — a runnable synthetic-data example

The zoom helper copies only ordinary data-coordinate lines; stack never
mutates its input arrays.

mplume intentionally does not wrap plotting calls or replace plt.subplots.
Not affiliated with OriginLab.

## License

MIT, see [LICENSE](LICENSE).
