# 2.	Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

num = int(input('Введи число: '))
i = 2
sp = []
while i * i <= num:
    while num % i == 0:
        sp.append(i)
        num = num // i
    i = i + 1
if num > 1:
    sp.append(num)

print(sp)
