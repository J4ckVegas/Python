class Person:
    name = "Ivan"
    age = 10

    def set(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    course = 1

Igor = Student()
Igor.set('Igor', 19)
Igor.course = 2
print('Name:',Igor.name,'Age:', Igor.age, 'Course:', Igor.course)

Vlad = Person()
Vlad.set ('Vlad', 25)
print(Vlad.name + " " + str(Vlad.age))

Ivan = Person()
Ivan.set("Ivan", 27)
print(Ivan.name, Ivan.age)

#Блокирующие поджопники
#Бестолковая хрень обходится легко
#Допустим если поджопники на __set, то пишем _Person__set (профит...)