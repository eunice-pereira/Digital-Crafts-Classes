class Mob: 
    def __init__(self, name, health = 10, power = 2): 
        self.name = name 
        self.health = health 
        self.power = power

    def get_hit(self, power): 
        self.health = self.health - power 
        print(f"I {self.name} was hit for {power} points and now have: \n {self.health}" 

    def attack(self, enemy): 
        enemy.get_hit(self.power)

class Hero(Mob): 
    def yell(self): 
        print("I %s, say to thou villian. Prepare to die!" % self.name)

hero = Hero("Clint")
print(hero.attack_power)
bad_guy = Mob("Baddy")
hero.attack(bad_guy)
print(bad_guy.health)
