import view
import model
import logging

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    level=logging.INFO)


def main_function():
    sel = view.hello()
    if sel == 1:
        #logging.INFO('Выбран калькулятор ')
        num = view.kalc()
        #logging.INFO('Выражение введено')
        rezult = model.work_kalc(num)
        #logging.INFO('Результат получен')
        view.printt(rezult)
        logging.INFO('Результат выведен на экран')
    elif sel == 2:
        logging.INFO('Выбран конвертер ')
        num = view.konverter()
        #logging.INFO('Масса введена')
        rezult = model.work_konverter(num)
        #logging.INFO('Результат получен')
        view.printt(rezult)
        logging.INFO('Результат выведен на экран')
