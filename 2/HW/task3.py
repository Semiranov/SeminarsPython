# Задайте список из n чисел последовательности(1 + 1 / n) ** n   2   2;2.25=4.25
# выведите на экран их сумму.

n = int(input('Введите число: '))
sum = 0
for i in range(1, n + 1):
    sum += (float(1 + 1 / i) ** i)
print(sum)