res = 0
x = int(input('Set X: '))
z = input('Выполняем операция: ')
y = int(input('Set y: '))

if z == '+':
    res = x + y
elif z == '-':
    res = x - y
elif z == '/':
    res = x / y
elif z == '*':
    res = x * y
else:
    print('Незивестная операция')
print('Result is',res)
