# 1.	Вычислить число c заданной точностью d
# Пример:	при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$

import math
num = input('Введите желаемую точность числа π: ')
pi = math.pi
print('π = ',pi)
i = -1
count = 0
if "." in num:
    while num[i] != '.':
        i += -1
        count += 1
    print(round(pi, count))
else:
    print('Error')


