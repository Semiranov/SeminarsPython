# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
import random

# konf = 100  #игра с человеком
# hod = random.randint(0, 1)
# print(f'Всего конфет: {konf}')
# while konf > 28:
#     if hod == 0:
#         player = 1
#     else: player = 2
#     kol = int(input(f'Игрок {player} Возьмите конфеты до 28 штук: '))
#     if 0 < kol <= 28 :
#         konf = konf - kol
#         print(f'Конфет осталось {konf} штук')
#         hod = (hod + 1) % 2
#     else:
#         print('Ошибка, вы взяли неверное колличество конфет')
#
# while konf > 0:
#     if hod == 0:
#         player = 1
#     else: player = 2
#     kol = int(input(f'Игрок {player} Возьмите конфеты до {konf} штук: '))
#     if 0 < kol < konf:
#         konf = konf - kol
#         print(f'Конфет осталось {konf} штук')
#     elif kol == konf:
#         print(f'Ура, игрок {player} выйграл')
#         konf = konf - kol
#     else:
#         print('Ошибка, вы взяли неверное колличество конфет')

konf = 50  # игра с ботом
hod = random.randint(0, 1)
while konf > 30:
    print(f'Конфет осталось {konf} штук')
    if hod == 0:
        kol = int(input(f'Игрок возьмите конфеты до 28 штук: '))
        if (0 < kol <= 28):
            konf = konf - kol
            hod = (hod + 1) % 2
        else:
            print('Ошибка, вы взяли неверное колличество конфет')

    elif hod == 1:
        kol = random.randint(1, 29)
        print(f'Бот берет: {kol}')
        konf = konf - kol
        hod = (hod + 1) % 2

while konf > 0:
    print(f'Конфет осталось {konf} штук')
    if hod == 0:
        kol = int(input(f'Игрок возьмите конфеты до {konf} штук: '))
        if (0 < kol <= konf):
            konf = konf - kol
            if konf == 0:
                print(f'Ура, игрок победил')
            else:
                hod = (hod + 1) % 2
        else:
            print('Ошибка, вы взяли неверное колличество конфет')
    elif hod == 1:
        if konf == 30:
            kol = 1
            print(f'Бот берет: {kol}')
            konf = konf - kol
            hod = (hod + 1) % 2
        if konf == 29:
            kol = random.randint(1, 29)
            print(f'Бот берет: {kol}')
            konf = konf - kol
            hod = (hod + 1) % 2
        elif konf  <= 28:
                kol = konf
                print(f'Бот берет: {kol}')
                print('Бот выйграл')
                hod = (hod + 1) % 2
                konf = konf - kol