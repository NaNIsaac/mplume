"""Explicit scientific Matplotlib rcParams presets and size helpers."""
from collections.abc import Mapping
from contextlib import contextmanager
import matplotlib as mpl
import matplotlib.pyplot as plt

STYLES = ("box", "house")
BASE = {
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "Liberation Sans", "DejaVu Sans"],
    "pdf.fonttype": 42, "ps.fonttype": 42, "svg.fonttype": "none",
    "savefig.dpi": 300, "axes.grid": False,
    "lines.linewidth": 1.5, "lines.markersize": 4.5,
    "legend.frameon": False,
}
VARIANTS = {
    "box": {
        "axes.spines.top": True, "axes.spines.right": True,
        "axes.linewidth": 1.0,
        "xtick.direction": "in", "ytick.direction": "in",
        "xtick.top": True, "ytick.right": True,
        "xtick.minor.visible": True, "ytick.minor.visible": True,
        "xtick.major.size": 5.5, "ytick.major.size": 5.5,
        "xtick.minor.size": 2.6, "ytick.minor.size": 2.6,
        "xtick.major.width": 1.2, "ytick.major.width": 1.2,
        "xtick.minor.width": 0.8, "ytick.minor.width": 0.8,
    },
    "house": {
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.linewidth": 0.9,
        "xtick.direction": "in", "ytick.direction": "in",
        "xtick.top": False, "ytick.right": False,
        "xtick.minor.visible": True, "ytick.minor.visible": True,
        "xtick.major.size": 4.5, "ytick.major.size": 4.5,
        "xtick.minor.size": 2.0, "ytick.minor.size": 2.0,
        "xtick.major.width": 0.9, "ytick.major.width": 0.9,
        "xtick.minor.width": 0.65, "ytick.minor.width": 0.65,
    },
}
CONTEXTS = {
    "paper": {"font.size": 9, "axes.labelsize": 9, "xtick.labelsize": 8,
              "ytick.labelsize": 8, "legend.fontsize": 8},
    "slide": {"font.size": 13, "axes.labelsize": 13, "xtick.labelsize": 11,
              "ytick.labelsize": 11, "legend.fontsize": 11, "lines.linewidth": 2.0},
    "poster": {"font.size": 18, "axes.labelsize": 18, "xtick.labelsize": 15,
               "ytick.labelsize": 15, "legend.fontsize": 15, "lines.linewidth": 2.5},
}
WIDTHS = {"single": 3.5, "double": 7.2}

def available_styles():
    return STYLES

def _params(variant, context, rc):
    if variant not in VARIANTS:
        raise ValueError(f"Unknown style {variant!r}; choose from {STYLES}")
    if context not in CONTEXTS:
        raise ValueError(f"Unknown context {context!r}; choose from {tuple(CONTEXTS)}")
    params = {**BASE, **VARIANTS[variant], **CONTEXTS[context]}
    if rc:
        params.update(rc)
    mpl.RcParams(params)
    return params

def use(variant="box", context="paper", *, rc: Mapping | None = None):
    """Set defaults for subsequent Matplotlib artists globally."""
    mpl.rcParams.update(_params(variant, context, rc))

@contextmanager
def style(variant="box", context="paper", *, rc: Mapping | None = None):
    """Temporary defaults; create and save figures within the context."""
    with mpl.rc_context(rc=_params(variant, context, rc)):
        yield

def _size(width, aspect):
    w = WIDTHS.get(width, width) if isinstance(width, str) else width
    if isinstance(w, str) or not isinstance(w, (int, float)) or w <= 0 or aspect <= 0:
        raise ValueError("Width and aspect must be positive; presets are 'single' and 'double'")
    return float(w), float(w * aspect)

def figure(width="single", *, aspect=0.75, **kwargs):
    return plt.subplots(figsize=_size(width, aspect), **kwargs)

def subplots(width="double", *, aspect=0.65, **kwargs):
    return plt.subplots(figsize=_size(width, aspect), **kwargs)

def panel_label(ax, label, *, x=0.02, y=0.98, **kwargs):
    opts = {"transform": ax.transAxes, "ha": "left", "va": "top",
            "fontweight": "bold", "clip_on": False}
    opts.update(kwargs)
    return ax.text(x, y, str(label), **opts)
