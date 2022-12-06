# 5.	Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
f1 = open('task5a.txt', 'r')
mn1 = f1.read()
f2 = open('task5b.txt', 'r')
mn2 = f2.read()
f1.close()
f2.close()
print(mn1)
print(mn2)

def newsp(spIN): #функция удаления всего лишнего кроме многочленов
    spIN = list(spIN)
    spOUT = []
    i = 0
    while i < len(spIN):
        if spIN[i] == 'x':
            i +=2
        elif spIN[i] == '+' or spIN[i] == ' ' or spIN[i] == '=' or spIN[i] == '-':
            i += 1
        else:
            spOUT.append(spIN[i])
            i += 1
    return spOUT

mn3 = newsp(mn1)
print(mn3)
mn4 = newsp(mn2)
print(mn4)