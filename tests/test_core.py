import matplotlib
matplotlib.use("Agg")
import matplotlib as mpl
import matplotlib.pyplot as plt
import pytest
import mplume as mp

def test_context_restores():
    before = mpl.rcParams["font.size"]
    with mp.style("box", "poster"):
        assert mpl.rcParams["font.size"] == 18
        assert mpl.rcParams["xtick.minor.visible"]
    assert mpl.rcParams["font.size"] == before

def test_invalid_style():
    with pytest.raises(ValueError):
        mp.use("invalid")

def test_figure_and_label():
    fig, ax = mp.figure("single", aspect=0.5)
    assert tuple(fig.get_size_inches()) == (3.5, 1.75)
    assert mp.panel_label(ax, "a").get_text() == "a"
    plt.close(fig)
