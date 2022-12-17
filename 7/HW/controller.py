import view, model

sprav = [['Иванов', 'Иван', '89271234587'],['Петров', 'Петр', '83651478521'],['Сидоров', 'Сергей', '89274589632']]
sprav2 = []

def main_function():
    num = view.hello()
    if num == 1:
        message = model.export_txt(sprav)
        view.print_export(message)
    elif num == 2:
        message = model.export_csv(sprav)
        view.print_export(message)
    elif num == 3:
        sp = model.import_txt(sprav2)
        view.print_import(sp)
    elif num == 4:
        sp = model.import_csv(sprav2)
        view.print_import(sp)