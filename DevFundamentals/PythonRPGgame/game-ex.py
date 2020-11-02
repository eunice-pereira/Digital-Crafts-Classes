from Unit import Unit, Player
from Item import Item, Potion

name = input ("What is the player's name? ")

player = Player(name, [5,5])

menu = ["Move up", "Move Down", "Move Left", "Move Right"]

enemies = [
    Unit("Orc", [4,4], 10, 2),
    Unit("Goblin", [6,6], 6, 3)
]

items = [
    Item("Treasure", [2,3]), 
    Potion("Health Potion", [3,3])
]

def show_menu(): 
    for i in range(len(menu)): # will put number on menu items 
        print(f"{i+1}. {menu[i]}")

    for item in player.inventory: 
        print(f"{i}. Use {item.name}")
        i += 1 

playing = True 

while playing:
     # show stats at beginning of every play 
    print(player.health, player.position)
    show_menu()
    try: 
        action = int(input("What is your choice? \n"))
    except ValueError: 
        print("You must enter a valid entry.")
        action = None 

    # moving character around 
    if action: 
        if action == 1: 
            player.move("up")
        elif action == 2: 
            player.move("down")
        elif action == 3: 
            player.move("left")
        elif action == 4: 
            player.move("right")
        else: 
            if action < len(player.inventory) - 4: 
                player.inventory[action - 4].use()

    # running into enemy, attack
    for enemy in enemies: 
        if enemy.position == player.position: 
            print(f"You ran into {enemy.name}:")
            print("You attack!")
            player.attack(enemy)
            print("Enemy attack!")
            enemy.attack(player)

    for item in items:
        if item.position == player.position: 
            if item.name == "Treasure": 
                playing = False #exits out of playing 
                print("You found the Treasure. You won the game!")
            else: 
                print(f"You have come across {item.name}")
                item.get_picked_up(player)
   