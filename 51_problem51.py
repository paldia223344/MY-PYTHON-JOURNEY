#Super constructor
class employee:
    def __init__(self):
        print("constructor of class employee")
    
class manager:
    def __init__(self):
        print("Constructor of class manager")
        
class deputy(manager):
     def __init__(self):
      super().__init__()
      print("Constructor of deputy")
              
d = deputy()

