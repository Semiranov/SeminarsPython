# 4.	Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите число: '))
sp = []
for i in range(-N, N+1):
    sp.append(i)
print(sp)

f = open('task4.txt', 'r')
a = int(f.read(1))
b = int(f.read(2))
print(f' В файле выбраны позиции {a} и {b}')
print(f' Произведение элементов на позициях {a} и {b} = {sp[a] * sp[b]}')
f.close()