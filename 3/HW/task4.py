# 4.	Напишите программу, которая будет преобразовывать десятичное число в двоичное
# (встроенными методами пользоваться нельзя).
# Пример:
# 	45 -> 101101
# 	3 -> 11
# 	2 -> 10

num = int(input('Введите число '))
sp = []
while num != 0:
    sp.append(num % 2)
    num //= 2

sp.reverse()
print(' '.join(map(str, sp)))
