# Instantiation - creating a self contained 'instance' of a class that can be used in the program.
# attributes - values in class that can be accessed using attritube (like key in dictionary)

# self is considered standard as the first parameter in every method, in every class 
# self is not an argument 

class Person: 
    def __init__(self, sport, truck, motorcycle, minivan): 
        self.sport = sport 
        self.truck = truck
        self.motorcycle = motorcycle 
        self.height = height

clint = Person("Clint", 38, "short")
anna = Person("Anna", 37)

print(f"Wow {clint.name} you are {clint.age} years old")
print(clint.height)
print(anna.height)