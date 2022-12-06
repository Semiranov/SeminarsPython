# 3.	Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# [1, 2, 2, 3, 4]  -> [1, 3, 4]
import math
import random

# num = int(input('введите длинну желаемого списка: '))
# sp = []
# for i in range(num):
#     sp.append(random.randint(0,10))
# print(sp)
sp = [10, 3, 1, 1, 10]
sp2 = []
a = sp.pop(0)
for i in range(len(sp)):
    if a not in sp:
        sp2.append(a)
        a = sp.pop(0)
    else:
        a = sp.pop(0)
print(sp2)



