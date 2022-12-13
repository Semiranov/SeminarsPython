import view
import model
import logging

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


def main_function():
    try:
        select = view.greeting()

        if select == 1:
            logging.INFO('Выбран режим калькулятор')
            primer = view.get_mat_example()
            result = model.calc(primer)
            view.view_result(result)
            logging.INFO(f'Выведен результат {result}')
        elif select == 2:
            logging.INFO('Выбран режим конвертер')
            massa = view.get_massa()
            logging.INFO(f'Введено значение {massa}')
            value = model.converter()
            view.view_result(value)
    except Exception as err:
        logging.warning(f'Введено не корректное значение', {err})
