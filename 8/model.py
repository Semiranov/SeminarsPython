import csv


def print_all_worcers():
    with open('data.csv', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=';')
        return list(file_reader)

def add_worker(sp):
    with open('data.csv',mode="a", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=";")
        file_writer.writerow(sp)


def change_data(num,sp):
    with open('data.csv', encoding='utf-8') as file:
        file_reader = list(csv.reader(file, delimiter=';'))
        print(file_reader)


