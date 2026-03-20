class Employee:
        language = "java"
        salary = 10000000
        def __init__(self,name,salary,language):
            self.name= name 
            self.language = language
            self.salary = salary
            
E1 = Employee("dia pal",100000000,"python")
print(E1.name,E1.salary,E1.language)
    