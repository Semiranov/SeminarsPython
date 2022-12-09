# 3.	Дан список чисел. Вывести из него только простые числа.

sp = [4, 5, 9, 14, 7]

def prime(n):
    count = 0
    for i in range(2, n//2 +1 ):
        if n % i == 0:
            count += 1
    if count > 0:
        return False

rez = list(filter(prime, sp))
print(rez)