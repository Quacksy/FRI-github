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
#Moremo spremenit tabelo v numericno da lahko ugotovimo lokacijo pik in lojter
print(zemljevid)