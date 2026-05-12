# property decorators 
class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f" The class value of a is {cls.a}")
        
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
    
        
# n = Employee()
# n.a = 56
# print(n.a)
# n.show()

e = Employee()
e.name = "Ravi Kumar"

print(e.fname, e.lname)