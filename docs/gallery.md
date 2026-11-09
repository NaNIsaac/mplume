# Figure gallery

Three reproducible plots, all based on deterministic synthetic signals. No measured data, image mockups or screenshots are used.

To generate actual vector figures using the installed mplume library:

```sh
python -m pip install -e '.[test]'
python examples/gallery.py --output examples/output
```

The script writes three **SVG** files:

| Figure | What it demonstrates | Output |
| --- | --- | --- |
| 01 · Zoom inset | Standard `Line2D` copy and highlighted zoom region | `01-zoom.svg` |
| 02 · Stacked scans | Display offsets; the original 2D input stays unchanged | `02-stack.svg` |
| 03 · Two panels | Matplotlib subplots and mplume panel labels | `03-panels.svg` |

The files are build artifacts, not hand-drawn illustrations. The CI workflow generates them and keeps them as a downloadable workflow artifact. A local run writes them under `examples/output/`.

All axes use arbitrary units. `stack` applies display-only offsets, **not** physical background subtraction. `zoom` copies simple data-coordinate lines, not scatter plots, images or custom transforms. See [composition](composition.md) for limitations.

Examples use the released **mplume 0.2.0** public API. Gallery generation is tested in CI so the README does not promise unsupported methods.
