"""Scientific Matplotlib styles and composition helpers."""
from .core import available_styles, figure, panel_label, style, subplots, use
from .inset import zoom
from .stack import StackResult, stack

__version__ = "0.2.0"
__all__ = ["use", "style", "figure", "subplots", "panel_label",
           "available_styles", "zoom", "stack", "StackResult"]
