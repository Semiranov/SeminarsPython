# 1.	Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

sp = [1, 2, 2, 3, 3, 3]
sp2 = []
for i in sp:
    if sp.count(i) == 1:
        sp2.append(i)

print(*sp2)