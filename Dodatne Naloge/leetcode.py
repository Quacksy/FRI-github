from subprocess import list2cmdline
import numpy as np

list1 = [1,2,4]
list2 = [1,3,4]
list3 = []

for a in list2:
    list3.append(a)
for a in list1:
    list3.append(a)
list3.sort()
print(list3)