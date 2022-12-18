import view
import model
import logging

logging.basicConfig(filename='log.txt',
                    encoding='utf8',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


def main_function():
    logging.info('Программа запущена')
    enter = view.welcome_function()
    if enter == 1:
        logging.info('Выбран 1')
        all_sp = model.print_all_worcers()
        view.printing(all_sp, 'Список всех сотрудников:')
        logging.info('Сработано')
    elif enter == 2:
        logging.info('Выбран 2')
        worker = view.add_in()
        model.add_worker(worker)
        view.printing(model.print_all_worcers(), 'Обновленный список сотрудников:')
        logging.info('Сработано')
    elif enter == 3:
        logging.info('Выбран 3')
        all_sp = model.print_all_worcers()
        num = view.change_worker(all_sp)
        change = view.add_in()
        change_sp = model.change_data(num, change)
        view.printing(model.print_all_worcers(), 'Обновленный список сотрудников:')
        logging.info('Сработано')
    elif enter == 4:
        logging.info('Выбран 4')
        all_sp = model.print_all_worcers()
        num_del = view.del_worker(all_sp)
        model.dell_data(num_del)
        view.printing(model.print_all_worcers(), 'Обновленный список сотрудников:')
        logging.info('Сработано')
    elif enter == 5:
        logging.info('Выбран 5')
        model.export_txt()
        view.printing(model.print_all_worcers(), 'Следующие данные экспортированы в файл data.txt')
        logging.info('Сработано')
    else:
        print('Ошибка ввода')
        logging.info('Ошибка ввода')
