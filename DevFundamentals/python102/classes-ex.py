class Vehicle: 
    def __init__(self, category, wheels = 4):  
        self.category = category 
        self.wheels = wheels 

minivan = Vehicle("Minivan")    
motorcycle = Vehicle("motorcycle", 2)

print(motorcycle.wheels)