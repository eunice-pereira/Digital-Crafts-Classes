# making class item for treasure 

class Item: 
    def __init__(self, name, position): 
        self.position = position 
        self.name = name 

class Potion(Item): 
    def __init__(self, name, position): 
        super().__init__(name,position)
        self.owner = None 
    
    def use(self): 
        self.owner.health += 10 
    
    def get_picked_up(self, owner): 
        self.owner = owner
        self.position = [-555, -555] #random range but prevents player from picking up item multiple times in same posiiton 
        