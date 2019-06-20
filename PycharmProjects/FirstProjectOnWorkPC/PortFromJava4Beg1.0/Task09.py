a = 'Сергей, 26 лет'
b = 'Jack 25 age'
l = [a, b]
while l.count('Stop') != 1:
    l.append(input('Задайте значение эллементу массива или напишите Stop: '))
else:
    l.remove('Stop')
print(l[:])