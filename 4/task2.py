# 2.	Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1.	с помощью математических формул нахождения корней квадратного уравнения
# 2.	с помощью дополнительных библиотек Python

import math

a, b, c = [int(i) for i in input('Введите значения переменных: ').split()]
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    print(f"x1 = {x1} x2 = {x2}")
elif d == 0:
    x1 = -b / (2 * a)
    print(f"x = {x1}")
else:
    print('Корней нет')
