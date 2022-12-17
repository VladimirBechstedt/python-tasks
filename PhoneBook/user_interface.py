def file_name():
    file = input('Введите имя файла: ')
    if file == '':
        return
    return file

def file_extension():
    extension = input('В каком расширении? ')
    if extension == '':
        return
    return extension

def menu():
    print('Введите 1 чтобы создать книгу номеров\n'
          '        2 чтобы открыть файл\n'
          '        3 чтобы выйти ')
    a = int(input('Ваш выбор: '))
    return a

def creating_list():
    print('Вводите фамилию и номер через точку "Иванов.89516543210" / чтобы закончить ввод, введите 0')
    lists = []
    while True:
        a = input()
        if a == '0':
            break
        lists.append(a)

    return lists