from turtle import right
import numpy as np

zemljevid = [
    "......",
    "..##..",
    ".##.#.",
    "...###",
    "###.##",
]

zemljevid = np.array(zemljevid)
zemljevid = zemljevid.reshape(5, 1)
print(zemljevid)