# Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно 5 и 10 или 15, но не 30.

num = int(input('ВВедите число'))
if num % 10 == 0 and (num % 15 == 0 or  num % 30 != 0):
    print('yes')
else:
    print('no')