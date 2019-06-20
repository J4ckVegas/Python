try:
    x = int(input('Enter num for X: '))
except ValueError:
    print('Вы ввели не число')
    x = 0
try:
    y = int(input('Enter num for Y: '))
except ValueError:
    print('Вы ввели не число')
    y = 0
else:
    print('Все верно')
finally:
    print('Выполнится 100%')

try:
    res = x / y
except ZeroDivisionError:
    print('Делить на ноль нельзя!')
    res = 0
print('Result is ', res)