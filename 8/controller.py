import view, model
import logging

logging.basicConfig(level=logging.INFO)


def main_function():
    enter = view.welcome_function()
    try:
        if not enter in [1,2,3,4]:
            raise ValueError
    except Exception: exit()
    if enter == 1:
        logging.INFO('Выбран 1')
        all_sp = model.print_all_worcers()
        view.printing(all_sp)
    elif enter == 2:
        logging.INFO('Выбран 2')
        worker = view.add_in()
        model.add_worker(worker)
        view.new_printing(model.print_all_worcers())
    elif enter == 3:
        logging.INFO('Выбран 3')
        all_sp = model.print_all_worcers()
        num = view.change_worker(all_sp)
        change = view.add_in()
        change_sp = model.change_data(num,change)
        view.new_printing(model.print_all_worcers())
    elif enter == 4:
        logging.INFO('Выбран 4')
        all_sp = model.print_all_worcers()
        num_del = view.del_worker(all_sp)
        model.dell_data(num_del)
        view.new_printing(model.print_all_worcers())
logging.INFO('Все ок')