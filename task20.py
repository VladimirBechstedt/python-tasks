def unpacking(file):
    f = open(file, 'r')
    n = (f.readlines())
    f.close()
    return n[0]

file1 = 'degeneration1.txt'
file2 = 'degeneration2.txt'

a = unpacking(file1) + ' = ' + unpacking(file2)
print(a)