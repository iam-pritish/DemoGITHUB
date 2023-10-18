a =55
print(a)

class sum:
  def __init__(self, add, sub):
    self.add = add
    self.sub = sub
  def display(self):
    print(self.add)
    print(self.sub)
num1 = sum(23 , 32)
num1.display()
sum.display(num1)
print("Print the add number" , num1.add)

# This is the example of OOPs concept where we can initite the class which helps to re-use the code in verious forms 
# It is very good concept to create lrager code into shorter formate.

class Emp:
  def __init__(self, id, salary, exp):
    self.id = id
    self.salary = salary
    self.exp = exp
  def diaplay(self):
    print(self.id)
    print(self.salary)
    print(self.exp)
emp1 = Emp(88 , 120000, "4 years 6 months")
emp1.diaplay()    
     
