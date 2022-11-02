# xs = [5, 4, -7, 42, 12, -3, -4, 11, 42, 2, 84]
# stevec = 0
# for i in xs:
#     if i == 42:
#         stevec += 1
#         if stevec == 1:
#             print('Bravo idijot')
# print('Število 42 se v seznamu pojavi', stevec, 'krat.')
from typing import List

# xb = ['foo', 'bar', 'baz', 'Waldo', 'foobar']
# for a in xs:
#     if a == 'Waldo':
#         print(True)


# videl_sem_42= 42 in xs
# print(videl_sem_42)
#
# videl_se_walda = 'Waldo' in xb
# print(videl_se_walda)
#
# vsi_veckratniki = all(lu % 42 == 0 for lu in xs)
# print(vsi_veckratniki)


# stevilo_uporbnik = int(input('vnesi stevilo:'))
# stevila = []
# delitelji=all(for i in range(1, 1000) if stevilo_uporbnik % i == 0)
# stevila.append(delitelji)
# print(delitelji)
# xs = [42, 5]
# veckratniki = True
#
# for vec in xs:
#     print(veckratniki)
#     print(vec)
#     if vec % 42 != 0:
#         veckratniki = False
# print(veckratniki)


# numbers = [('I', 1),
#            ('V', 5),
#            ('X', 10),
#            ('L', 50),
#            ('C', 100),
#            ('D', 500),
#            ('M', 1000),]
# s = "MCMXCIV"
# s = s.replace("IV", "IIII").replace("IX", "VIIII")
# s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
# s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
# answer = 0
# for roman, num in numbers:
#     for i in s:
#         if i == roman:
#             answer = answer + num
#
# print(answer)
# print(s)
