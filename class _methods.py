class employee:
    a = 1
    #implementing class method
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")
 
p = employee()
p.a = 90 
p.show()       