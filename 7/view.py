import controller


def hello():
    select = int(input('Привет: \n 1 - калькулятор \n 2 - конвертер'))
    return select


def kalc():
    primer = input('Введите выражение: ')
    return primer


def konverter():
    kg = int(input('Введите килограммы: '))
    return kg


def printt(rez):
    print(f'Результат равен {rez}')
