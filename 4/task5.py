# 5.	Вам дан словарь, состоящий из пар слов.
# Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
# Для слова из словаря, записанного в последней строке, определите его синоним.

slovar = {}
slovar['Hello'] = 'Hi'
slovar['Bye'] = 'Goodbye'
slovar['List'] = 'Array'
print(slovar)
slovo = input('Введите слово синоним которого вы ищите')
for key, value in slovar.items():
    if slovo == key:
        print(value)
    if slovo == value:
        print(key)