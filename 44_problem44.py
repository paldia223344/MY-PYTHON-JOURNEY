class Employee:
    language = 'JAVA'
    salary = 1200000
    
    def getinfo(self):
        #self.language = "Python"
        print(f"EMPLOYEE DETAILS:")
        print(f"language: {self.language} , salary : {self.salary}")

e1 = Employee() #object created
e1.getinfo()