class mother:
    mothername = ""
    
    def mother(self):
        print(self.mothername)

class father():
    fathername = ""
    
    def father(self):
        print(f"Father name is {self.fathername}")
            
class son(father,  mother):
      def parents(self):
            print("Father name is ", self.fathername)
            print("Mother name is ", self.mothername)
    
      def father(self):
        print(f"Father name is {self.fathername}")
            
s1 = son()
s1.fathername = "Ravi Kumar"
s1.mothername = "Sita Devi"
s1.parents()
