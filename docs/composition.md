# Composition: insets and stacked curves

mplume is an add-on to Matplotlib, not a plotting engine. Keep using
Matplotlib subplots and GridSpec for multipanel layouts.

## Zoom inset

Use mp.zoom(ax, xlim=(0.1, 0.8), ylim=(0.6, 1.1)).
It returns a standard inset Axes. By default, simple data-coordinate Line2D
curves are copied from the parent and a highlight box and connectors are drawn.
Set connect=False to omit connectors. Change location with loc="upper left",
"upper right", "lower left", "lower right" or "center"; size=0.35 is
relative to the parent axes. bounds=(left,bottom,width,height) overrides placement.

Scatter, images, errorbar caps, filled areas, custom transforms, and future
updates of parent line data are not copied. Use copy_lines=False and draw these
yourself on the returned inset Axes.

## Stacked curves

mp.stack(ax, x, patterns, normalize="max", spacing="auto",
         labels=["A", "B", "C"])

patterns is a two-dimensional numeric array of shape (number of curves,
number of x values). The operation preserves its input. normalize="max"
divides each curve by its maximum absolute intensity; default None leaves
intensity units unchanged before display offsets. The result object exposes
lines, offsets and values (the plotted data). Explicit spacing is measured
in post-normalization y units. direction="down" reverses stacking direction.

Automatic spacing uses 1.15 times the largest peak-to-peak variation, and
does not guarantee non-overlap when baselines differ. Additive offsets should
not be used on logarithmic axes without reconsidering their physical meaning.
Document display shifts in captions; they are not background subtraction.

## Example

See examples/scientific.py for a reproducible synthetic-data example.
