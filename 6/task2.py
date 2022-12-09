# 2.	На первой строке вводится натуральное число N — количество строк.
# Далее следуют N строк, которые надо будет отсортировать

string = []
num = int(input('Введите число'))
for i in range(num):
    st = input(f'Введите {i+1} строку: ')
    string.append(st)

string.sort(key=lambda  x: len(x))
print(*string, sep='\n')