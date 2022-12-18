import view, model


def main_function():
    enter = view.welcome_function()
    if enter == 1:
        all_sp = model.print_all_worcers()
        view.printing(all_sp)
    elif enter == 2:
        worker = view.add_in()
        model.add_worker(worker)
    elif enter == 3:
        all_sp = model.print_all_worcers()
        view.change_worker(all_sp)
