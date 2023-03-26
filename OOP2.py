class Person:
    def __init__(self, firstname, lastname, age, country):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.skills = []
    def get_perrson_info(self):
        return f'He is {self.firstname} {self.lastname}. He is from {self.country}. He is {self.age} years old.'
    def add_skill(self, skill):
        self.skills.append(skill)
    def get_skills(self):
        return ', '.join(self.skills)
        
p = Person('John', 'Doe', 25, 'UK')
print(p)
print(p.get_perrson_info())

# p2 = Person()
# print(p2.get_person_info())
# print(p2.skills)
p.add_skill('HTML')
p.add_skill('CSS')
p.add_skill('JS')
p.add_skill('React')
p.add_skill('Python')
print(p.get_skills())

# Inheritence // creating a child / creating is gone be so easy using python
# 

class Student(Person):
    def __init__(self, firstname, lastname, age, country, gender):
        self.gender = gender
        super().__init__(firstname, lastname, age, country)
        
    def get_perrson_info(self):
        pronoun = 'He' if self.gender == 'Male' else 'She'
        # return super().get_perrson_info()
        
s = Student('Elina', 'Sami',21, 'Finland', 'Female')
print(s.firstname)
print(s.get_perrson_info())


# value = 'TRUE VALUE' if 4 < 2 else 'False value'
# print(value)    
