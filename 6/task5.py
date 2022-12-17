# Напишите программу для обработки текста.
# На вход вашей программы подаётся многострочный текст,
# Ваша задача – пронумеровать слова в нём, начиная с нуля, а затем вывести только те слова, которые начинаются с большой буквы.
# Перед словом необходимо вывести номер первого вхождения этого слова в текст.
# Слова необходимо отсортировать в лексикографическом порядке. (В решении задачи поможет функция enumerate())

st = ['Ехал Грека через реку.','Видит Грека в реке рак.','Сунул в реку руку Грека.','Рак за руку Греку цап.']
#
# st_num = list(enumerate(st))
# print(st_num)
res = []
for s in st:
    res.extend(s.replace('.','').split())
print(res)
res = list(enumerate(res))
print(res)
res.sort(key=lambda x: x[1])
print(res)
res = list(filter(lambda x: x[1][0].isupper(), res))
print(res)
result = []
for s in res:
    if s[1] not in result:
        result.append(s[1])
        print(f'{s[0]} - {s[1]}')