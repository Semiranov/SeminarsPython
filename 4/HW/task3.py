# 3.	Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# [1, 2, 2, 3, 4]  -> [1, 3, 4]

import random

num = int(input('введите длинну желаемого списка: '))
sp = []
for i in range(num):
    sp.append(random.randint(0,10))
print(sp)

sp2 = []
for i in range(len(sp)):
    if sp.count(sp[i]) == 1:
        sp2.append(sp[i])
print(sp2)



