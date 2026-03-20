class calculations:
    def __init__(self,num):
        self.square = num**2
        self.cube  = num**3
        self.squareroot = num**0.5
        
num = int(input("Enter a number:"))
calc = calculations(num)
print(calc.square,calc.cube,calc.squareroot)