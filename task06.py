a = input('Введите число: ')
p = 0

for i in a:
    if 0 < int(i) < 10:
        p += int(i)

print(p)