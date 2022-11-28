# 2.	Определите среднее значение всех элементов последовательности, завершающейся числом 0.

# num = int(input('Введите число '))
# sum = num
# count = 0
# while num != 0:
#     num = int(input('Введите число '))
#     count += 1
#     sum += num
# print(round(sum/count, 2))

n = None
sp = []
while n != 0:
    n = int(input('Вводите числа'))
    sp.append(n)

print(sum(sp)/(len(sp)-1))