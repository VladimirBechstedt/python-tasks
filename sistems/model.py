import csv
import json


employee = []

def read_csv():
    global employee
    with open('database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin, delimiter=',')
        for row in csv_reader:
            temp = {}
            temp['id'] = int(row[0])
            temp['last_name'] = row[1]
            temp['first_name'] = row[2]
            temp['position'] = row[3]
            temp['phone_number'] = row[4]
            temp['salary'] = float(row[5])
            employee.append(temp)

def employee_list():
    return employee

def search_by_name(name):
    return (list(filter(lambda x: x['first_name'] == name, employee)))

def search_by_position(position):
    return (list(filter(lambda x: x['position'] == position, employee)))

def search_by_salary(salary):
    return (list(filter(lambda x: salary[0] <= x['salary'] <= salary[1], employee)))

def add_employee(last_name, first_name, position, phone_number, salary):
    global employee
    temp = {}
    temp['id'] = employee[len(employee) - 1]['id'] + 1 if len(employee) > 0 else 1
    temp['last_name'] = last_name
    temp['first_name'] = first_name
    temp['position'] = position
    temp['phone_number'] = phone_number
    temp['salary'] = salary
    employee.append(temp)

def delete(id):
    global employee
    try:
        index = (next(i for i, x in enumerate(employee) if x['id'] == id))
        employee.pop(index)
    except StopIteration:
        print('error')

def update_data(id, last_name, first_name, position, phone_number, salary):
    global employee
    temp = {}
    temp['id'] = id
    temp['last_name'] = last_name
    temp['first_name'] = first_name
    temp['position'] = position
    temp['phone_number'] = phone_number
    temp['salary'] = salary
    try:
        index = (next(i for i, x in enumerate(employee) if x['id'] == id))
        employee[index] = temp
    except StopIteration:
        print('error')

def write_csv():
    with open('database.csv', 'w', encoding='utf-8') as fin:
        names = ['id', 'last_name', 'first_name', 'position', 'phone_number', 'salary']
        csv_write = csv.DictWriter(fin, fieldnames=names, lineterminator='\n')
        for row in employee:
            csv_write.writerow(row)

def write_json():
    with open('database.json', 'w', encoding='utf-8') as fin:
        json.dump(employee, fin)