field = [[' '] * 3 for i in range(3)]

def great():
    print('------------------------')
    print('    Приветствуем вас    ')
    print('         в игре         ')
    print('    "Крестики-нолики"   ')
    print('------------------------')
    print('формат ввода: x y       ')
    print(' x - номер строки       ')
    print(' y - номер столбца      ')


great()
def show():
    print(f'  | 0 | 1 | 2 |')
    print(f'---------------')
    for i in range(3):
     row_info = ' | '.join(field[i])    
     print(f'{i} | {row_info} |')
     print('---------------')

def ask():
    while True:
       ward =input('        Ваш ход:').split()

       if len(ward) != 2:
           print('Введите 2 координаты!')
           continue

       x, y = ward

       if not(x.isdigit()) or not(y.isdigit()):
           print('Введите числа!')
           continue

       x, y = int(x), int(y)

       if 0 > x or x > 2  or 0 > y or y > 2:
           print('Координаты вне диапазона! ')
           continue

       if field[x][y] != ' ':
           print('Клетка занята!')
           continue


       return x, y


def check_win():
    win_ward = (((0,1),(0,2),(0,0)), ((1,1),(1,0),(1,2)), ((2,1),(2,2),(2,0)),
                ((0,2),(1,1),(2,0)), ((0,0),(1,1),(2,2)), ((1,0),(2,0),(0,0)),
                ((0,1),(1,1),(2,1)), ((2,2),(0,2),(1,2)))
    for ward in win_ward:
        simba = []

        for s in ward:
            simba.append(field[s[0]][s[1]])
        if simba == ['X','X','X']:
            print('Выйграл X!!!')
            return True
        if simba == ['0','0','0']:
            print('Выйграл 0!!!')
            return True
    return False

num = 0
while True:
    num +=1

    show()

    if num % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if check_win():
        break

    if num == 9:
        print('Ничья')
        break

