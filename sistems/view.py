def show_menu():
    print('\n' + '=' * 20)
    print('Выберите необходимое действие')
    print('1. Найти сотрудника')
    print('2. Сделать выборку сотрудников по должности')
    print('3. Сделать выборку сотрудников по зарплате')
    print('4. Добавить сотрудника')
    print('5. Удалить сотрудника')
    print('6. Обновить данные сотрудника')
    print('7. Экспортировать данные в формате json')
    print('8. Экспортировать данные в формате cmv')
    print('9. Закончить работу')
    return int(input('Ввыберите номер необходимого действия: '))

def display_data(data):
    print('-' * 30)
    print('| id |   Фамилия   |   Имя    |  Должность  | Номер телефона | Зарплата |')
    for i in data:
        print('| ' + str(i['id']) + (' ' * (3 - len(str(i['id'])))) + '| ' + i['last_name'] + (' ' * (12 - len(i['last_name']))) + '| ' + i['first_name'] + (' ' * (9 - len(i['first_name']))) + '| ' + i['position'] + (' ' * (12 - len(i['position']))) + '| ' + i['phone_number'] + (' ' * (15 - len(i['phone_number']))) + '| ' + str(i['salary']) + (' ' * (9 - len(str(i['salary'])))) + '|')

def in_data(message):
    return input(f'{message}: ')


def pause():
    print('Чтобы продолжить нажмите Enter')
    input()