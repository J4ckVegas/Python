l = []
lis = [1, 56, 'x', 34, 2.34, ['s', 't', 'r', 'o', 'k', 'a']]
print (lis)

a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print(a)

l.append(23) #Добавить значение в конец списка
l.append(34) #Добавить значение в конец списка
b = [24, 67]
l.extend(b) #Прибавить список к списку
l.insert(1, 56) #Добавить значение на выбранный индекс
l.append(34)
l.remove(34) #Удаление элемента по знач (только 1)
l.pop(0) #Удаление элемента по индексу
print (l.index(67))
print (l.count(34)) #Считает элементы
l.sort()#Сортировка, без значения сорт по возраст
l.reverse() #Развернуть список
print(l)
#print(l.clear()) Очистить список