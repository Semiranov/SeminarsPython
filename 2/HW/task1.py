# 1.	Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.

# num = input('Введите вещественное число ')
# sum = 0
# for i in range(len(num)):
#     if num[i] != '.':
#         sum += int(num[i])
# print(sum)

num = input('Введите вещественное число ')
sum = 0
for i in range(len(num)):
    if num[i].isdigit():
        sum += int(num[i])
print(sum)
