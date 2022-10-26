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

for _ in zemljevid:
    for a in _:
        for b in a:
            print(b)
