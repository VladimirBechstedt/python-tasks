# Это первая версия испровленая версия будет позже

from random import randint

def out():
    print(f'''      1   2   3
    1 {a[0][0]} | {a[0][1]} | {a[0][2]}
      ---------
    2 {a[1][0]} | {a[1][1]} | {a[1][2]}
      ---------
    3 {a[2][0]} | {a[2][1]} | {a[2][2]}''')

def typing(p):
    global a
    print(f'Ход {p}')
    a[int(input('Строка: ')) - 1][int(input('Столбец: ')) - 1] = p


def draw(x, o):
    p = x if randint(0, 1) == 0 else o
    print('Первым ходит ', p)
    return p

def check(player, play):
    if (a[0][0] == player and a[0][1] == player and a[0][2] == player) or\
        (a[1][0] == player and a[1][1] == player and a[1][2] == player) or\
        (a[2][0] == player and a[2][1] == player and a[2][2] == player) or\
        (a[0][0] == player and a[1][0] == player and a[2][0] == player) or\
        (a[0][1] == player and a[1][1] == player and a[2][1] == player) or\
        (a[0][2] == player and a[1][2] == player and a[2][2] == player) or\
        (a[0][0] == player and a[1][1] == player and a[2][2] == player) or\
        (a[0][2] == player and a[1][1] == player and a[2][0] == player):
        out()
        print(player, 'победил')
        return False
    else:
        return True

def change(p):
    return 'O' if p == 'X' else 'X'

def main():
    player = draw('X', 'O')
    play = True
    while play:
        out()
        typing(player)
        play = check(player, play)
        player = change(player)


a = [[' ', ' ', ' '],
     [' ', ' ', ' '],
     [' ', ' ', ' ']]

main()