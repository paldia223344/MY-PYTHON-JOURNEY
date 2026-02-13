class calculator():
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f" square of a number is {self.n*self.n}")
        
    def cube(self):
        print(f" cube of a number is {self.n**3}")
            
    def squareroot(self):
        print(f" square of a number is {self.n**(1/2)}")
        
a = calculator(2)
a.square()
a.cube()
a.squareroot()
