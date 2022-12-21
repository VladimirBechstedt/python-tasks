import model
import view

def launch():
    model.read_csv()
    view.display_data(model.employee_list())
    while True:
        numder_menu = view.show_menu()
        if numder_menu == 1:
            a = model.search_by_name(view.in_data('Имя'))
            view.display_data(a)
            view.pause()
        if numder_menu == 2:
            a = model.search_by_position(view.in_data('Должность'))
            view.display_data(a)
            view.pause()
        if numder_menu == 3:
            b = model.search_by_salary((float(view.in_data('От')), float(view.in_data('До'))))
            view.display_data(b)
            view.pause()
        if numder_menu == 4:
            surname = view.in_data('Фамилия')
            name = view.in_data('Имя')
            position = view.in_data('Должность')
            number = view.in_data('Номер телефона')
            salary = float(view.in_data('Зарплата'))
            model.add_employee(surname, name, position, number, salary)
            model.write_csv()
            view.display_data(model.employee_list())
            view.pause()
        if numder_menu == 5:
            view.display_data(model.employee_list())
            model.delete(int(view.in_data('Введите id работника чтобы его удалить')))
            model.write_csv()
            view.display_data(model.employee_list())
            view.pause()
        if numder_menu == 6:
            view.display_data(model.employee_list())
            _id_ = int(view.in_data('Введите id работника чтобы обновить дынные'))
            surname = view.in_data('Фамилия')
            name = view.in_data('Имя')
            position = view.in_data('Должность')
            number = view.in_data('Номер телефона')
            salary = float(view.in_data('Зарплата'))
            model.update_data(_id_, surname, name, position, number, salary)
            model.write_csv()
            view.display_data(model.employee_list())
            view.pause()
        if numder_menu == 7:
            model.write_csv()
        if numder_menu == 8:
            model.write_json()
        if numder_menu == 9:
            break