i = 1
while i < 100:
    print(i)
    i *= 2
print(i)

for j in 'hello world\n':
    if j == 'w':
        continue #Пропуск итерации
    print(j * 2, end = '')

for k in 'hello world\n':
    if k == 'w':
        break #Выход из цикла
    print(k * 2, end = '')

for q in 'hello world\n':
    if q == 'a':
        break #Выход из цикла
    print(q * 2, end = '')
else:
    print("Буквы а нету в слове")