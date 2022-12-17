from user_interface import file_name as fn
from user_interface import file_extension as fe
from working_with_data import packing

def reading(a):
    with open(f'{a}.txt', 'r', encoding='utf-8') as f:
        dataList = [i.replace('\n', '') for i in f.readlines()]
    return dataList

def record(a, b, data):
    if a == None:
        a = 'newfile'
        print(a)
    if b == None:
        b = 'txt'
    with open(f'{a}.{b}', 'w', encoding='utf-8') as f:
        for i in data:
            f.write(i + '\n')
