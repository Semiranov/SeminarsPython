import csv


def export_txt(sp):
    f = open('sprav.txt', 'w')
    for i in sp:
        f.write('\n'.join(i))
        f.write('\n')
    f.close()
    return 'sprav.txt'


def export_csv(sp):
    f = open('sprav.csv', 'w')
    count = 1
    for i in sp:
        wr = csv.writer(f, delimiter=";", lineterminator="\r")
        wr.writerow(i)
    f.close()
    return 'sprav.csv'



def import_txt(sp):
    f = open('sprav.txt', 'r')
    sp.append(f.readlines())
    f.close()
    return sp

def import_csv(sp):
    f = open('sprav.csv', 'r')
    read = csv.reader(f, delimiter=";")
    sp.append(list(read))
    f.close()
    return sp