from random import randint

def winer(p1, p2, f, b):
    if f == p1 and b % 2 == 0:
        return p1
    elif f == p1 and b % 2 == 1:
        return p2
    elif f == p2 and b % 2 == 0:
        return p2
    elif f == p2 and b % 2 == 1:
        return p1

def with_a_person(sweets):
    b = 0
    Player1 = input('Имя первого игрока: ')
    Player2 = input('Имя второго игрока: ')
    furst = Player1 if randint(1, 2) == 1 else Player2
    print(f'Первым играет {furst}')
    while sweets >= 28:
        c = True
        while c:
            try:
                a = int(input('Сколько конфет вы берёте: '))
                c = False if 0 < a <= 28 else True
            except ValueError:
                pass

        print('\033[4m\033[31m\033[44m{}\033[0m' .format('Ход переходит следующему'))
        sweets -= a
        b += 1

    winner = winer(Player1, Player2, furst, b)
    print(f'Осталось {sweets} конфет и их забирает {winner}')
    print(f'{winner} выиграл!!!')

def with_a_bot(sweets):
    b = 0
    Player1 = input('Имя первого игрока: ')
    Player2 = 'Бот'
    print(f'Против вас играет {Player2}')
    furst = Player1 if randint(1, 2) == 1 else Player2
    print(f'Первым играет {furst}')
    if furst == Player1:
        play = True
        while play:
            if play:
                c = True
                while c:
                    try:
                        a = int(input('Сколько конфет вы берёте: '))
                        c = False if 0 < a <= 28 else True
                    except ValueError:
                        pass

                print('\033[4m\033[31m\033[44m{}\033[0m'.format('Ход переходит следующему'))
                sweets -= a
                b += 1
                play = True if sweets >= 28 else False

            if play:
                bot = randint(1, 28)
                print(f'Бот берёт {bot} конфет')
                print('\033[4m\033[31m\033[44m{}\033[0m'.format('Ход переходит следующему'))
                sweets -= bot
                b += 1
                play = True if sweets >= 28 else False
    else:
        play = True
        while play:
            if play:
                bot = randint(1, 28)
                print(f'Бот берёт {bot} конфет')
                print('\033[4m\033[31m\033[44m{}\033[0m'.format('Ход переходит следующему'))
                sweets -= bot
                b += 1
                play = True if sweets >= 28 else False

            if play:
                c = True
                while c:
                    try:
                        a = int(input('Сколько конфет вы берёте: '))
                        c = False if 0 < a <= 28 else True
                    except ValueError:
                        pass

                print('\033[4m\033[31m\033[44m{}\033[0m'.format('Ход переходит следующему'))
                sweets -= a
                b += 1
                play = True if sweets >= 28 else False

    winner = winer(Player1, Player2, furst, b)
    print(f'Осталось {sweets} конфет и их забирает {winner}')
    print(f'{winner} выиграл!!!')

def with_a_smart_bot(sweets):
    b = 0
    Player1 = input('Имя первого игрока: ')
    Player2 = 'Бот'
    print(f'Против вас играет {Player2}')
    furst = Player1 if randint(1, 2) == 1 else Player2
    print(f'Первым играет {furst}')
    if furst == Player1:
        play = True
        while play:
            if play:
                c = True
                while c:
                    a = int(input('Сколько конфет вы берёте: '))
                    c = False if a <= 28 else True
                print('Ход переходит следующему')
                sweets -= a
                b += 1
                play = True if sweets >= 28 else False

            if play:
                q = sweets - 29
                bot = q if 0 < q < 29 else 28
                print(f'Бот берёт {bot} конфет')
                print('Ход переходит следующему')
                sweets -= bot
                b += 1
                play = True if sweets >= 28 else False
    else:
        play = True
        while play:
            if play:
                q = sweets - 29
                bot = q if 0 < q < 29 else 28
                print(f'Бот берёт {bot} конфет')
                print('Ход переходит следующему')
                sweets -= bot
                b += 1
                play = True if sweets >= 28 else False

            if play:
                c = True
                while c:
                    a = int(input('Сколько конфет вы берёте: '))
                    c = False if a <= 28 else True
                print('Ход переходит следующему')
                sweets -= a
                b += 1
                play = True if sweets >= 28 else False

    winner = winer(Player1, Player2, furst, b)
    print(f'Осталось {sweets} конфет и их забирает {winner}')
    print(f'{winner} выиграл!!!')

print('''С кем вы хотите играть?
      Если с другом введите 1
      Если с ботом введите 2
      Если с умным ботом введите 3''')
while True:
    try:
        choice = int(input('Ваш выбор? '))
        if 0 < choice < 4:
            break
    except ValueError:
        pass

CANDIES = 200

if (choice == 1): with_a_person(CANDIES)
if (choice == 2): with_a_bot(CANDIES)
if (choice == 3): with_a_smart_bot(CANDIES)