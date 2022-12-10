a = 'абв'
b = 'сегодня было прохладно и безветренно'

for i in a:
    b = b.replace(i, '')

print(b)