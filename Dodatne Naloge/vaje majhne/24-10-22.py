import numpy as np
import sys
from math import sqrt, sin, cos

# print(sqrt(44))
# print(sys.getsizeof(3.11))
# print(sys.getsizeof(3))


# a = np.zeros(5)
# print(a)
#
# b = np.zeros(5, dtype= int)
# print(b)
#
# c = np.ones(5, dtype= float)
# print(c)
#
# aa = np.empty(10, int)
# print(aa)
#
# bb = np.full(10, 44)
# print(bb)
#
# d2 = np.full((4, 3), 4)
# print(d2)
#
# k = np.arange(5)
# print(k)
#
dodatek = np.linspace(0, 3.5, 15)
print(dodatek)
#
# rand = np.random.randint(0, 100, (4, 3))
# print(rand)


# d = np.array([2, 6, 8])
# f = np.array([1, 8, 9])
# print(d + f)
#
# naj = np.max(d)
# print(naj)
#
# man = np.min(d)
# print(man)
#
# poprecje = np.mean(d)
# print(poprecje)

# r = np.random.randint(1, 100, (10, 10))
# print(r)
#
# ocena = np.full(r.shape, "", dtype=object)
# print(ocena)
#
# ocena[r < 30] = ["bravo"]
# ocena[r > 30] = ['vadi misko']
# ocena[r == 99] = ["ti pa si en rene"]
# print(ocena)


# iskanje tock v krogu
# N = 1_000_000
# t = np.random.random((N, 2)) * 2 - 1
# #print(t)
#
# a = np.sum(np.sum(t ** 2, axis=1) < 1) * 4 / N
# print(a)



