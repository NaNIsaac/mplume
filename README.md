# mplume

Publication-ready scientific styles for Matplotlib.

Version 0.1.0: `box` and `house` styles, `paper`/`slide`/`poster` contexts, optional figure sizing and panel labels.

```python
import matplotlib.pyplot as plt
import mplume as mp

with mp.style('box', 'paper'):
    fig, ax = mp.figure('single')
    ax.plot([1, 2, 3], [2, 1, 3])
    mp.panel_label(ax, 'a')
    fig.savefig('figure.pdf')
```

`pip install mplume` will be supported after the first PyPI release. Source installation: `pip install git+https://github.com/NaNIsaac/mplume.git`.

See the source for the complete 0.1.0 API. Not affiliated with OriginLab.
