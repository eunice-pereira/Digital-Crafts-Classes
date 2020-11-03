# tip calculator 2 

tip = 0

while tip == 0: 
    bill = float(input("Total bill amount?:"))
    split = int(input("Split how many ways?:"))
    serv = input("Level of service? Enter good, fair, or bad:")

    if serv == "good": 
        tip = float(bill * .2)

    elif serv == "fair": 
        tip = float(bill * .15)

    elif serv == "bad":
        tip = float(bill * .10)

    else: 
        print("Please enter good, fair, or bad only.")
    
total = bill + tip
split_amt = total/split

print("Tip amount: $%.2f" % tip)
print("Total amount: $%.2f" % total)
print("Amount per person: $%.2f" % split_amt)