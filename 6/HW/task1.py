# 1.	Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел.
# Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел.
# Ввод чисел продолжается до ввода пустой строки.
# Входные данные	Выходные данные
# 36
# 12
# 144
# 18	             6
from math import gcd
from functools import reduce

sp = []
while True:
    a = input('Введи числа: ')
    if a != '':
        sp.append(int(a))
    else: break

print(reduce(gcd, sp))