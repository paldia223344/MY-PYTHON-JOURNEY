class player:
      def __init__(self,name,age):
          self.name = name
          self.age = age
          
class footballer(player):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Constructor of footballer class is called")
        
    def show(self):
        print(self.name," is of age" , self.age)
        print("Constructor of player class is called")
        
p = footballer("BHARAT", 23)
p.show()

        