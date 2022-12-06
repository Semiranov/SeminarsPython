# 2.	Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков и определяет,
# можно ли из этих отрезков составить треугольник.
# Входные данные	Выходные данные
# triangle(1, 1, 2)	Это не треугольник
# triangle(7, 6, 10)  Это треугольник

def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


a = 7
b = 6
c = 10

print(triangle(a, b, c))
