f = open ("text.txt", 'w')
#print(f.read())
#for line in f:
#   print(line)
f.write('Hi, it\'s me!\nTest')
f.close()






# 'r' - Открытие на чтение (является значение по умолчанию)
# 'w' - открытие на запись, содержимое файла удаляется, если файла не существует, создается новый
# 'x' - открытие на запись, если файла не существует, иначе исключение
# 'a' - открытие на дозапись, информаци ядобавляется в конец файла
# 'b' - открытие в двоичном режиме
# 't' - открытие в текстовом режиме (является значением по умолчанию
# '+' - открытие на чтение и запись