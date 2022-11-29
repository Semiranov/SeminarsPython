# 3.	Реализуйте алгоритм задания случайных чисел без использования встроенного
# генератора псевдослучайных чисел.
# Подсказка: можно использовать модуль datetime

import time



def myrandom(n):
    strT = str(time.time())
    strT = strT.replace('.', '')
    num = int(strT) % n
    return num

print(myrandom(1000))