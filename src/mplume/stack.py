"""Non-destructive display offsets for scientific curves."""
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class StackResult:
    lines: tuple
    offsets: np.ndarray
    values: np.ndarray

def stack(ax, x, ys, *, spacing="auto", normalize=None,
          labels=None, direction="up", **plot_kwargs):
    """Stack rows of a 2D intensity array; return lines and applied offsets."""
    x = np.asarray(x)
    data = np.asarray(ys, dtype=float)
    if x.ndim != 1 or not x.size or data.ndim != 2 or data.shape[1] != x.size or not len(data):
        raise ValueError("x must be 1D and ys must have shape (n_series, len(x))")
    if not np.isfinite(data).all():
        raise ValueError("ys must be finite")
    if normalize not in (None, "max"):
        raise ValueError("normalize must be None or 'max'")
    if direction not in ("up", "down"):
        raise ValueError("direction must be 'up' or 'down'")
    if labels is not None and len(labels) != len(data):
        raise ValueError("labels count must match ys")
    values = data.copy()
    if normalize == "max":
        maximum = np.max(np.abs(values), axis=1)
        values /= np.where(maximum == 0, 1, maximum)[:, None]
    if spacing == "auto":
        gap = 1.15 * max(float(np.ptp(values, axis=1).max()), 1e-12)
    else:
        try:
            gap = float(spacing)
        except (TypeError, ValueError) as exc:
            raise ValueError("spacing must be 'auto' or non-negative") from exc
        if not np.isfinite(gap) or gap < 0:
            raise ValueError("spacing must be finite and non-negative")
    offsets = (1 if direction == "up" else -1) * gap * np.arange(len(data))
    lines = []
    for i, (series, offset) in enumerate(zip(values, offsets)):
        kwargs = dict(plot_kwargs)
        if labels is not None:
            kwargs["label"] = str(labels[i])
        line, = ax.plot(x, series + offset, **kwargs)
        lines.append(line)
    return StackResult(tuple(lines), offsets, values + offsets[:, None])
