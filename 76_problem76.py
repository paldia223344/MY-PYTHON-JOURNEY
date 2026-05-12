class Animal:
    def __init__(self,name):
        self.name = name 
        
    def info(self):
        print(f"Animal name is  {self.name}")
       
       
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def details(self):
        print(self.name, "is a ", self.breed)
        
        
dog1 = Dog("Buddy" , "Golden Retriever")
dog1.info()
dog1.details()