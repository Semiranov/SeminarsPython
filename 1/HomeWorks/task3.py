# 3.	Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).

X = int(input('Введите координату X'))
Y = int(input('Введите координату Y'))
if X > 0 and Y > 0:
    print('Точка находится в 1й четверти')
elif X < 0 and Y > 0:
    print('Точка находится во 2й четверти')
elif X < 0 and Y < 0:
    print('Точка находится в 3й четверти')
elif X > 0 and Y < 0:
    print('Точка находится в 4й четверти')
else:
    print('Error')