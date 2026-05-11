class Employee:
    def __init__(self):
        print("Employee class constructor is called")
    a = 1
    
class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer class is called")
    b = 2
    
class Manager(Programmer, Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of class Manager is called ")
    c = 3
  
o = Employee()
p = Programmer()
m = Manager()
print(o.a, p.b, m.c)

