# 1.	Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

num = int(input('Введите число обозначающую день недели'))
if num > 0 and num < 6:
    print('Это будний день')
elif num == 6 or num == 7:
    print('Это выходной день')
else:
    print('Ошибка')