# Напишите программу которая на вход будет приниимать число N и
# выводить числа от -N до N

N = int(input('Введите число'))
for i in range(-N, N + 1):
    print(i, end=" ")

# N = int(input('Введите число'))
# revN = -N
# while revN != (N + 1):
#     print(revN, end=" ")
#     revN += 1

