num = input("Введите ваше имя: ")

if num == "Test":
    print("True")
else:
    print("Привет,",num)

num1 = int(input("Введите число: "))

if num1 > 0:
    print("Вы ввели число больше 0")
elif num1 < 0:
    print("Вы ввели число меньше 0")
else:
    print ("Вы ввели число 0")

Name = input()
A = 'Yes!' if Name != "Test" else 'No'
print(A)