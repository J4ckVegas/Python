class Person:
    name = "Ivan"
    age = 10

    def set(self, name, age):
        self.name = name
        self.age = age

Vlad = Person()
Vlad.set ('Vlad', 25)
print(Vlad.name + " " + str(Vlad.age))

Ivan = Person()
Ivan.set("Ivan", 27)
print(Ivan.name, Ivan.age)

