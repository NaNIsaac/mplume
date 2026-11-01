"""Zoom inset helper for ordinary Matplotlib line plots."""
from matplotlib.lines import Line2D

def zoom(ax, xlim, ylim, *, loc="upper right", size=0.35,
         connect=True, copy_lines=True, bounds=None, **kwargs):
    """Return an inset Axes. Only simple data-coordinate lines are copied.

    bounds optionally specifies (left, bottom, width, height) in ax coordinates.
    """
    if len(xlim) != 2 or len(ylim) != 2 or xlim[0] >= xlim[1] or ylim[0] >= ylim[1]:
        raise ValueError("xlim and ylim must be increasing two-element sequences")
    positions = {"upper right": (1-size-0.05, 1-size-0.05),
                 "upper left": (0.05, 1-size-0.05),
                 "lower right": (1-size-0.05, 0.05),
                 "lower left": (0.05, 0.05),
                 "center": ((1-size)/2, (1-size)/2)}
    if bounds is None:
        if not 0 < size <= 0.9:
            raise ValueError("size must be positive and at most 0.9")
        if loc not in positions:
            raise ValueError("Unknown inset location")
        bounds = (*positions[loc], size, size)
    if len(bounds) != 4 or bounds[2] <= 0 or bounds[3] <= 0:
        raise ValueError("bounds must have positive width and height")
    inset = ax.inset_axes(bounds, transform=ax.transAxes, **kwargs)
    if copy_lines:
        for line in ax.lines:
            if not isinstance(line, Line2D) or line.get_transform() != ax.transData:
                continue
            inset.plot(*line.get_data(), color=line.get_color(),
                       linewidth=line.get_linewidth(), linestyle=line.get_linestyle(),
                       marker=line.get_marker(), markersize=line.get_markersize(),
                       alpha=line.get_alpha())
    inset.set(xlim=xlim, ylim=ylim)
    inset.tick_params(labelsize="small")
    if connect:
        ax.indicate_inset_zoom(inset, edgecolor="0.35")
    return inset
