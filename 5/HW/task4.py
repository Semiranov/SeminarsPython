# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# st = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'

f1 = open('task4a.txt', 'r')  #чтение из файла
st = f1.read()
f1.close()
print(st)
sp = []
count = 1
j =0
for i in range(1, len(st)):
    if st[i] == st[i - 1]:
        count += 1
    else:
        sp.append(str(count) + st[i-1])
        count = 1
sp.append(str(count)+ st[-1])
st2 = ''.join(sp)
print(st2)
f2 = open('task4b.txt', 'w')  #запись в файл
f2.write(st2)
f2.close()

sp2 = []      #дешифровка
st3 = ''
for i in range(len(st2)):
    if st2[i].isdigit():
        st3 = st3 + st2[i]
    else:
        sp2.append(str(st2[i]) * int(st3))
        st3 = ''
print(''.join(sp2))