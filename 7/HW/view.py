def hello():
    enter_num = int(input('Привет, что будем делать? \n'
                      '1 - экспорт данных из списка в файл .txt \n'
                      '2 - экспорт данных из списка в файл .csv \n'
                      '3 - импорт данных из .txt в список \n'
                      '4 - импорт данных из .csv в список \n'))
    return enter_num



def print_export(mess):
    print(f'Экспорт прошел успешно создан файл {mess}')



def print_import(sp):
    print(f'Импорт прошел успешно создан список {sp}')