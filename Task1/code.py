import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


def findProb(trials=10000):
    square = [['blue', 'red', 'red', 'red', 'red'],
              ['red', 'red', 'blue', 'red', 'blue'],
              ['red', 'red', 'red', 'red', 'red'],
              ['blue', 'red', 'red', 'red', 'red'],
              ['red', 'red', 'red', 'red', 'red']]

    hits = np.zeros((5, 5), dtype=int)

    blue_hits = 0
    red_hits = 0
    for _ in range(trials):
        row = int(np.random.uniform(0, 5))
        col = int(np.random.uniform(0, 5))
        hits[row, col] += 1
        if square[row][col] == 'blue':
            blue_hits += 1
        else:
            red_hits += 1

    prob_blue = blue_hits / trials
    prob_red = red_hits / trials

    color_map = {'blue': 0, 'red': 1}
    grid_colors = np.array([[color_map[cell] for cell in row] for row in square])
    cmap = ListedColormap(['blue', 'red'])

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.imshow(grid_colors, cmap=cmap, origin='upper')

    for i in range(5):
        for j in range(5):
            count = hits[i, j]
            ax.text(j, i, str(count),
                    ha='center', va='center',
                    fontsize=12, fontweight='bold', color='white')

    ax.set_xticks(range(5))
    ax.set_yticks(range(5))
    ax.set_xticklabels(range(1, 6))
    ax.set_yticklabels(range(1, 6))
    ax.set_title(
        f'Геометрическая вероятность (бросков: {trials})\n'
        f'P(синий) ≈ {prob_blue:.5f}, P(красный) ≈ {prob_red:.5f}'
    )

    ax.set_xticks(np.arange(-0.5, 5, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 5, 1), minor=True)
    ax.grid(which='minor', color='black', linewidth=1.5)
    ax.tick_params(which='major', size=0)

    plt.tight_layout()
    plt.show()

    return prob_blue, prob_red


p_blue, p_red = findProb(20000)
