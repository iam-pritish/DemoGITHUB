print("Hello Everyone...!!")

class Emp:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)
emp1 = Emp ('Pritish', 27)
emp1.display()

emp2 = Emp ('Prajyot', 26)
Emp.display(emp2)

print("This Employee-01 has Name:- ", emp1.name)
print("This Employee-02 age is:-", emp2.age)
