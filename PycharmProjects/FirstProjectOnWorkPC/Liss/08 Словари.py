d = {'test' : 1, 'kek' : 5, 'lol' : 22}
print(d)
print(d['lol'])

d2 = dict(short='dict', longer='dictionary')
d2['short'] = 234
print(d2)

d3 = dict ([(23, 34), (56, 87)])
print(d3)

d4 = dict.fromkeys(['a', 'b', 'c'], 1)
print(d4)

d5 = {a : a ** 2 for a in range(7)}
print(d5)

person = {'name' : {'last_name': 'Иванов', 'first_name': 'Иван', 'middle_name': 'Иванович'}, 'address': ['г. Андрюшки', 'ул. Васильковская д. 23б', 'кв.12'], 'phone': {'home_phone': '34-67-12', 'mobile_phone': '8-564-345-23-65', 'mobile_phone_2': 'Нет'}}
print (person['name']['first_name'],person['name']['middle_name'], person['name']['last_name'])
print (person['address'])
print(person['phone']['home_phone'], person['phone']['mobile_phone'], person['phone']['mobile_phone_2'])