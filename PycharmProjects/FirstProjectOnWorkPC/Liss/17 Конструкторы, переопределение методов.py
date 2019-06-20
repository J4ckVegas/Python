class Person:
    name = "Ivan"
    age = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    course = 1

Igor = Student("Igor", 19)
#Igor.set('Igor', 19)
Igor.course = 2
print('Name:',Igor.name,'Age:', Igor.age, 'Course:', Igor.course)

Vlad = Person("Vlad", 25)
#Vlad.set ('Vlad', 25)
print(Vlad.name + " " + str(Vlad.age))

Ivan = Person("Ivan", 27)
#Ivan.set("Ivan", 27)
print(Ivan.name, Ivan.age)

