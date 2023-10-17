print("Hello Everyone...!!")

class Emp:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)
emp1 = Emp ('Pritish', 27)
emp1.dispay()

emp2 = Emp ('Prajyot', 26)
Emp.display(emp2)