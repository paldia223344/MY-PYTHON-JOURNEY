class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f" The class value of a is {cls.a}")
        
n = Employee()
n.a = 56
print(n.a)
n.show()