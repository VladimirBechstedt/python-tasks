
datalist = []

def init(data):
    global datalist
    datalist = data

def unpacking():

    for i in datalist:
        print(i.replace('.', ' - '))

def packing():
    a = []
    for i in datalist:
        a.append(i.replace('.', ':'))
    return a
