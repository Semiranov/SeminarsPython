# 5.	Реализуйте алгоритм перемешивания списка
# (shuffle использовать нельзя, другие методы из библиотеки random - можно).

import random

sp = ['один',2,'+','Москва',5,'Андрей',77,'???','@',10]
for i in range(len(sp)):
    j = random.randint(0, len(sp) - 1)
    sp[j], sp[i] = sp[i], sp[j]
print(sp)