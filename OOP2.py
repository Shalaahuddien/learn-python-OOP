class Person:
    def __init__(self, firstname, lastname, age, country):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
    def get_person_info(self):
        return f'He is {self.firstname} {self.lastname}. He is from {self.country}. He is {self.age}.'

p = Person('John', 'Doe', 25, 'UK')
print(p)
print(p.get_person_info())