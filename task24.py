f = open('file.txt', 'r', encoding='utf-8')
p = f.readlines(0)
p = p[0].replace('\n', '')
f.close()

i = 0
strin = ''
while i < len(p):
    o = p.count(p[i])
    strin += (f'{o}{p[i]}')
    i += o

f = open('fileOut.txt', 'w', encoding='utf-8')
f.write(strin)
f.close()
print(strin)