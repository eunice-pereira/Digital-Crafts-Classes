class Vehicle: 
    def __init__(self, top_speed, acceleration, wheels = 4):
        self.wheels = wheels 
        self.top_speed = int(top_speed)
        self.acceleration = int(acceleration)
        self.position = 0 # will always start at 0, not delcared as attribute in def
        self.speed = 0 # no flexibility to change 
        # self.race_stats = [] #empty list to save stats 

    def move(self):
        self.accelerate() 
        self.position += self.speed 
        # self.race_stats.append({"speed" :self.speed, "position" : self.position})
        # every time car moves, stats append to array line 8 

    def accelerate(self):
        self.speed += self.acceleration
        if self.speed > self.top_speed: 
            self.speed = self.top_speed
    
    def reset(self): 
        self.position = 0 
        self.speed = 0

# dictionary is clean way to list items
all_cars = {
    "camaro" : Vehicle(100,4), 
    "volvo" : Vehicle(80,6), 
    "focus" : Vehicle(60,2), 
    "Fiat" : Vehicle(120,3)
}

# function to run race 
def run_race(time): 
    for car_name in all_cars: 
        all_cars[car_name].reset()
        
    for sec in range(time): 
       for car_name in all_cars: 
            all_cars[car_name].move()
            # print(f"{car_name} -- {cur_car.speed} m/s") 

    print("Race is over!")
    for car_name in all_cars: 
        print(f" {car_name} - {all_cars[car_name].position}")

# for car_name in all_cars: 
#     print(f" {car_name}: ")
#     for i in range(len(all_cars[car_name].race_stats)):
#         print(all_cars[car_name].race_stats[i])

print("20 second run!")
run_race(20)

print("40 second run!")
run_race(40)

print("60 second run!")
run_race(60)