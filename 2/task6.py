# 6.	Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

# st = 'кооличооествоооо'
# st2 = 'оо'
# print(st.count(st2))

st = 'кооличооествоооо'
st2 = 'оо'
i = 0
count = 0
while i < len(st):
    if st[i:i + len(st2)] == st2:
        count += 1
        i += len(st2) - 1
    i += 1
print(count)