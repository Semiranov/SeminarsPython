# 4.	Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите степень К: '))
sp = []
for i in range(k + 1):
    sp.append(random.randint(0, 101))
    sp.append(f'x{k} + ')
    k -= 1
del sp[-1]
sp.append(' = 0')
st = ''.join(map(str, sp))
print(st)
f = open('task4.txt', 'w')
f.write(st)
f.close()
