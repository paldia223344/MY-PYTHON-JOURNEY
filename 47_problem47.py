'''
OOP Exercise 1: Create a Class with instance attributes
'''
class S:
    occupation = "service"
    def __init__ (self,salary,name,age):
        self.salary = salary
        self.name = name
        self.age = age
        
E1 = S(560000000,"Dia Pal",16)
print(E1.salary)