#Double inheritance
class Employee:
    name = "Default name"
    company = "INFOSYS"
    def show(self):
        print(f"name is {self.name} ")
        print(f"company is {self.company} ")
        
class coder:
    language = "JAVA"
    def info(self):
        print(f"language used by the coder is {self.language}")
 
class programmer(Employee,coder):
    age = 45
    def printoutputs(self):
        print(f"name is {self.name}")
        print(f"company is {self.company}")
        print(f"age is {self.age}")
        print(f"language is {self.language}")
        
        
a = programmer()
a.show()
a.info()
a.printoutputs()
           