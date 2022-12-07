# 5.	Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
f1 = open('task5a.txt', 'r')
mn1 = f1.read()
f2 = open('task5b.txt', 'r')
mn2 = f2.read()
f1.close()
f2.close()
print(f'многочлен в первом файле: {mn1}')
print(f'многочлен во втором файле: {mn2}')

def newsp(spIN): #функция удаления всего лишнего кроме многочленов
    spIN = list(spIN)
    spOUT = []
    i = 0
    while i < len(spIN) - 1:
        if spIN[i] == 'x':
            i +=2
        elif spIN[i] == '+' or spIN[i] == ' ' or spIN[i] == '=' or spIN[i] == '-':
            i += 1
        else:
            spOUT.append(spIN[i])
            i += 1
    return spOUT

mn3 = newsp(mn1)
print(f'список коэфицентов 1го многочлена: {mn3}')
mn4 = newsp(mn2)
print(f'список коэфицентов 2го многочлена: {mn4}')

mn5 = []
count = len(mn3) - 1
for i in range(len(mn3)):  #формируем список с суммами
    mn5.append(int(mn3[i]) + int(mn4[i]))
    mn5.append(f'x{count} + ')
    count -= 1
del mn5[-1]
mn5.append(' = 0')
st = ''.join(map(str, mn5))

f = open('task5c.txt', 'w') #Запись в файл
f.write(st)
f.close()