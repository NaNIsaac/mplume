import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pytest
import mplume as mp

def test_zoom():
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2], [1, 2, 0], color="red")
    inset = mp.zoom(ax, (0, 1), (0, 3))
    assert len(inset.lines) == 1
    assert inset.lines[0].get_color() == "red"
    assert tuple(inset.get_xlim()) == (0, 1)
    plt.close(fig)

def test_zoom_manual_and_invalid():
    fig, ax = plt.subplots()
    assert not mp.zoom(ax, (0, 1), (0, 1), copy_lines=False).lines
    with pytest.raises(ValueError):
        mp.zoom(ax, (2, 1), (0, 1))
    plt.close(fig)

def test_stack_preserves_data():
    fig, ax = plt.subplots()
    data = np.array([[0., 2., 0.], [0., 4., 0.]])
    original = data.copy()
    result = mp.stack(ax, [1, 2, 3], data, spacing=3)
    assert np.array_equal(data, original)
    assert np.array_equal(result.offsets, [0, 3])
    assert np.array_equal(result.values[1], [3, 7, 3])
    plt.close(fig)

def test_stack_normalize_and_bad_input():
    fig, ax = plt.subplots()
    result = mp.stack(ax, [0, 1], [[0, 0], [0, 4]],
                      normalize="max", labels=["a", "b"])
    assert np.isfinite(result.values).all()
    assert result.lines[1].get_label() == "b"
    with pytest.raises(ValueError):
        mp.stack(ax, [0, 1], [[0, 1, 2]])
    plt.close(fig)
