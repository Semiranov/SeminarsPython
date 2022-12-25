import csv, logging
import sqlite3

conn = sqlite3.connect('workers.db')
cursor = conn.cursor()


# def print_all_worcers():
#     with open('data.csv', 'r', encoding='utf-8') as file:
#         file_reader = csv.reader(file, delimiter=';')
#         return list(file_reader)

def print_all_worcers():
    cursor.execute('select * from workers')
    rezults = cursor.fetchall()
    print(rezults)


def add_worker(sp):
    with open('data.csv', "a", encoding='utf-8', newline='') as file:
        file_writer = csv.writer(file, delimiter=";")
        file_writer.writerow(sp)


def change_data(num, sp):
    try:
        with open('data.csv', 'r', encoding='utf-8') as file:
            file_reader = list(csv.reader(file, delimiter=';'))
            file_reader[num] = sp
        with open('data.csv', "w", encoding='utf-8', newline='') as file:
            file_writer = csv.writer(file, delimiter=";")
            for i in file_reader:
                file_writer.writerow(i)
    except IndexError:
        print('Вышли за границы массива')
        logging.info('Вышли за границы массива')
        exit()
    except Exception:
        print('Ошибка файла')
        logging.info('Ошибка файла')
        exit()


def dell_data(num):
    with open('data.csv', 'r', encoding='utf-8') as file:
        file_reader = list(csv.reader(file, delimiter=';'))
        del file_reader[num]
    with open('data.csv', "w", encoding='utf-8', newline='') as file:
        file_writer = csv.writer(file, delimiter=";")
        for i in file_reader:
            file_writer.writerow(i)


def export_txt():
    with open('data.csv', 'r', encoding='utf-8') as file:
        reader = list(csv.reader(file, delimiter=';'))
    with open('data.txt', 'w', encoding='utf-8') as file:
        for i in reader:
            file.write(';'.join(i))
            file.write('\n')
