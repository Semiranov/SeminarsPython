# 2.	Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

num = int(input('Enter number: '))
sp = []
while num % 2 == 0:
    num = num // 2
    sp.append(2)
while num % 3 == 0:
    num = num // 3
    sp.append(3)
while num % 5 == 0:
    num = num // 5
    sp.append(5)
if num == 1:
    print(f'Список простых множетелей: {sp}')
else:
    sp.append(num)
    print(f'Список простых множетелей: {sp}')
