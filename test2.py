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
