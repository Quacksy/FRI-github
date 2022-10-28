from distutils.log import set_verbosity
from turtle import right
from typing import overload
import numpy as np


#Segrevanje
ovire = ".##..####...##"
pregled = []
steevec = 1
for i in ovire:
    if i == '#':
        pregled.append(steevec)
    steevec += 1
print(pregled)




# zemljevid = [
#     "......",
#     "..##..",
#     ".##.#.",
#     "...###",
#     "###.##",
# ]

# zemljevid = np.array(zemljevid)
# zemljevid = zemljevid.reshape(5, 1)
# #Moremo spremenit tabelo v numericno da lahko ugotovimo lokacijo pik in lojter
# print(zemljevid)
