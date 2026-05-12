class Animal:
    def __init__(self,name):
        self.name = name 
        
    def info(self):
        print(f"Animal name is {self.name}")
        
class Dog(Animal):
    def sound(self):
        print(self.name,"barks")
        
D1 = Dog("Buddy")
D1.info()
D1.sound()

