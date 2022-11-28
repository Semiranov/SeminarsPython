# 5.	Удалить вторую цифру трёхзначного числа.

# num = 123
# print(num // 100,num % 10, sep='')

num = str(123)
print(num[0] + num[2])