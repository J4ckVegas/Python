import random


x = random.randrange(0, 10)
print('Сгенерировано случайное число от 0 до 9, попробуйте отгадать его, у Вас 3 попытки.')
limit = 0
index = 3

while True:

    try:
        y = int(input("Введите число: "))
    except ValueError:
        print('Вы ввели не число!!!')
        print('Значит будет: 0')
        y = 0

    index -= 1

    if y > x:
        print("Подсказка! Число меньше -", y, ' Осталось попыток: ', index)

    if y < x:
        print("Подсказка! Число больше -", y, ' Осталось попыток: ', index)

    if x == y:
        print('Вы победили!!!')
        r = input('Попробовать еще раз? (y/n): ')
        if r == 'y':
            print('Сгенерировано случайное число от 0 до 9, попробуйте отгадать его, у Вас 3 попытки.')
            x = random.randrange(0, 10)
            index = 3
        elif r == 'n':
            print('GameOver')
            break
        else:
            print('Ничего не понял, но видимо «Нет» \n GameOver')
            break
    if index == limit:
        print('Вы проиграли =(')
        r = input('Продолжить? (y/n): ')
        if r == 'y':
            print('Сгенерировано случайное число от 0 до 9, попробуйте отгадать его, у Вас 3 попытки.')
            x = random.randrange(0, 10)
            index = 3
        elif r == 'n':
            print('GameOver')
            break
        else:
            print('Ничего не понял, но видимо «Нет» \n GameOver')
            break
