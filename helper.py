#
# グラフ描画へルパ
#
from typing import List, Optional, Tuple
from matplotlib import pyplot as plt

from matplotlib.axes import Axes
from matplotlib.axis import Axis
import numpy as np

from src import Fuzzy


def init_canvas(figsize: Tuple[int, int], size: Tuple[int, int]) -> List[Axis]:
    if len(size) != 2:
        raise ValueError("size must be width,height")

    plt.figure(figsize=figsize, facecolor="#EEE")
    return [plt.subplot(size[0], size[1], n + 1) for n in range(size[0] + size[1] - 1)]


def draw(sets: List[Fuzzy], to: Axes, primaryindex: Optional[Tuple[int]] = None):

    for index, fuzzy in enumerate(sets):
        padding = 0.00
        linecolor = "#333"
        linestyle = "solid"
        has_scatter = True

        # プライマリインデックスならパディングする(意味不明)
        if primaryindex is not None:
            if index in primaryindex:
                padding = 0.02
                linecolor = "#A00"
                has_scatter = False
            else:
                linecolor = "#666"
                linestyle = "dashed"

        # 描画
        underlying = fuzzy.base
        values = np.array(list(fuzzy.grade.values())) + padding
        label = fuzzy.namenode.latex_repr
        to.plot(underlying, values, color=linecolor, linestyle=linestyle, label=f"${label}$")

        if has_scatter:
            to.scatter(underlying, values, color="#444", s=20)

    to.grid(which="both", color="#DADADA")
    to.legend()
    to.set_xticks(underlying)
    to.set_yticks(np.arange(0.0, 1.1, 0.1))
    plt.xlim((min(underlying), max(underlying)))
