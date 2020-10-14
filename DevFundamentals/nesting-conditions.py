name = input("What is your name?")
num = len(name)
    # multiple conditions allowed. Both conditions must be met in order to be true (run)

if num > 3 and num < 15: 
    if num == 4: 
        print("Perfect length!")
    else: 
        print("It's an ok length.")
    print(f"Welcome {name}.")
else: 
    print(f"{num} is not a good number of characters.")

