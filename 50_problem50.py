# Multi level inheritance
class Employee:
    a = 1
    
class programmer(Employee):
        b = 5
    
class Manager(programmer):
    c = 3
    
n = Employee()
print(f"{n.a}")
m = programmer()
print(f"{m.a}")
print(f"{m.b}")
o = Manager()  
print(f"{o.b}")
print(f"{o.c}")