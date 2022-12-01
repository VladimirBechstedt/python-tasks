k = int(input('Введите число: '))
a = [0, 1]

for i in range(k - 1):
    a.append(a[len(a)-2] + a[len(a)-1])
    a.insert(0, a[1] - a[0])

a.insert(0, a[1] - a[0])
print(a)