class Player(Unit): 
    def __init__(self, name, position, health =10, attack_power = 2): 
        super().__init__(name, position, health, attack_power)
        self.inventory = [] 
        # store player treasure 
    
    def 