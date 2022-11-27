# Напишите программу котрая на вход принимает 5 чисел и нах макс из них
num = int(input('Введите число'))
max = num
for i in range(4):
    num = int(input('Введите число'))
    if num > max:
        max = num
print(f' Максимальноя число равняется {max}')

# sp = list()
# for i in range(5):
#     num = int(input('Введите число'))
#     sp.append(num)
# print(f' Максимальноя число равняется {max(sp)}')

