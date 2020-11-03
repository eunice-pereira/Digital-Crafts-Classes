# how many coins? 

coins = 0
more = "yes"

while more == "yes": 
    print(f"You have {coins} coins.")
    more = input("Do you want another?")

    if more == "yes": 
        coins += 1
if more == "no": 
    coins == coins 
    print(f"You have {coins} coins. Bye!")