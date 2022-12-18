def welcome_function():
    enter = int(input('Привет, что будем делать? \n'
                      '1 - отобразить список всех сотрудников \n'
                      '2 - добавить сотрудника \n'
                      '3 - изменить данные сотрудника \n'
                      '4 - удалить сотрудника \n'
                      '5 - экспортировать файд в .txt'))
    return enter


def printing(sp, string):
    print(string)
    for i, st in enumerate(sp):
        if i == 0:
            print(' ', *st)
        else:
            print(i, *st)


def add_in():
    worker = input('Введите данные сотрудника в формате Фамилия Имя Телефон Должность').split()
    return worker


def change_worker(sp):
    print('Введите номер сотрудника, которому нужно изменить данные: ')
    for i, st in enumerate(sp):
        if i == 0:
            print(' ', *st)
        else:
            print(i, *st)
    num = int(input())
    return num


def del_worker(sp):
    print('Введите номер сотрудника, которого нужно удалить: ')
    for i, st in enumerate(sp):
        if i == 0:
            print(' ', *st)
        else:
            print(i, *st)
    num = int(input())
    return num
