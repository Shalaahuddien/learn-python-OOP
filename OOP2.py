class Person:
    def __init__(self, firstname ='Asab', lastname = 'Yetayeh', age = 250, country = 'Findland'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
    def get_person_info(self):
        return f'He is {self.firstname} {self.lastname}. He is from {self.country}. He is {self.age} years old.'

p = Person('John', 'Doe', 25, 'UK')
print(p)
print(p.get_person_info())

p2 = Person()
print(p2.get_person_info())
