class Person:
    def __init__(self, firstname ='Asab', lastname = 'Yetayeh', age = 250, country = 'Findland'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.skills = []
    def get_person_info(self):
        return f'He is {self.firstname} {self.lastname}. He is from {self.country}. He is {self.age} years old.'
    def add_skill(self, skill):
        self.skills.append(skill)
    def get_skill(self):
        return ', '.join(self.skills)
        
p = Person('John', 'Doe', 25, 'UK')
print(p)
print(p.get_person_info())

p2 = Person()
print(p2.get_person_info())
print(p2.skills)
p2.add_skill('HTML')
p2.add_skill('CSS')
p2.add_skill('JS')
p2.add_skill('React')
p2.add_skill('Python')
print(p2.get_skill())

