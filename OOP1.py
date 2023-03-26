# Class

class Dog:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

d = Dog('Fluffy',8, 'Greece')
print(d.name)
print(d.age)
print(d.country)
