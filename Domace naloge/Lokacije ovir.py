import numpy as np


#Segrevanje
# ovire = ".##..####...##"
# pregled = []
# pregled = np.array(pregled)

# for lok in enumerate(ovire,start=1):
#     if lok[1] == "#":
#         if lok[0 + 1] == :

#         pregled = np.append(pregled,lok[0])

# pregled = np.reshape(pregled, (len(pregled) // 2, 2))
# print(pregled)
    





zemljevid = [
    "......",
    "..##..",
    ".##.#.",
    "...###",
    "###.##",
]

zemljevid = np.array(zemljevid)
zemljevid = zemljevid.reshape(len(zemljevid), 1)
tabela = []
#Moremo spremenit tabelo v numericno da lahko ugotovimo lokacijo pik in lojter
stevec = 1
for a in zemljevid:
    for b in a:
        for c in enumerate(b, start=1):
            if c[1] == "#" and c[1]:
                tabela.append([c[0], stevec])
    stevec += 1
print(tabela)
