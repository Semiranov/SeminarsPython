# 3.	Создайте программу для игры в "Крестики-нолики".
pole = [['-','-','-'],['-','-','-'],['-','-','-']]
print(*pole,sep='\n')
for k in range(9):
    i = int(input('Введите новер строки: '))
    j = int(input('Введите новер столбца: '))
    if pole[i][j] != '-':
        print('Занято!')
    else:
        pole[i][j] = input('Введите x или o: ')
        if (pole[0][0] == pole[0][1] == pole[0][2] != '-' or
            pole[1][0] == pole[1][1] == pole[1][2] != '-' or
            pole[2][0] == pole[2][1] == pole[2][2] != '-' or
            pole[0][0] == pole[1][1] == pole[2][2] != '-' or
            pole[2][0] == pole[1][1] == pole[0][2] != '-'):
                if pole[i][j] == 'x':
                    print('X победили!!!')
                    break
                else:
                    print('О победили!!!')
                    break


    print(*pole, sep='\n')