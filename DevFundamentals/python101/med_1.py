# tip calculator 

bill = float(input("Total bill amount?:"))
tip = 0

while tip == 0: 
    serv = input("Level of service? Enter good, fair, or bad:")

    if serv == "good": 
        tip = float(bill * .2)

    elif serv == "fair": 
        tip = float(bill * .15)

    elif serv == "bad":
        tip = float(bill * .10)

    else: 
        print("Please enter good, fair, or bad only.")
    
total = float(bill + tip)

print("Tip amount: $%.2f" % tip)
print("Total amount: $%.2f" % total)