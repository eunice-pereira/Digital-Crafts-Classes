# lists are datatypes 
# items in list can be of variable value 
# lists can contain mixture of strings, integers, variables, booleans. 

# ex. 1 

# favorite_foods = ["veggie pizza", "tofu banh mi", "veggie pho"]

# print(favorite_foods[2]

# ex. 2-3

things = ["coffee cup", "books", "monitor", "notebook"]

count = 1
for i in range(len(things)):
    print(f"{count}:", things[i])   
    count += 1


i = input("Which item is most interesting? Pick 1, 2, or 3:")

if i == "1": 
    print("You chose", things[0],"you must like coffee!")
    
elif i == "2": 
        print("You chose", things[1], "you must like to read.")
elif i == "3": 
        print("you chose",things[2], "you must like to work with computers.")
else: 
    print("You chose", things[3], "you must like to write.")