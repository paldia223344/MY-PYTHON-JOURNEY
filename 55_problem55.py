class vehicle:
 class Vehicle:
        company = "typre"   # class variable

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
        print(f"{self.name}, {self.max_speed}, {self.mileage}")


# Example usage
a = Vehicle("Dia Pal", 100, "beg")
print(a.company)   # prints "typre"

# Change class variable for all
Vehicle.company = "ttss"
print(a.company)   # prints "ttss"

b = Bus("City Bus", 80, 12)
print(b.company)   # prints "ttss"