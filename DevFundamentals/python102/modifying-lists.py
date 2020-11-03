my_pets = ["Daisy", "Molly", "Shadow"]

# .append() is a data type method that can add single item to end of list

# my_pets.append("Rainbow")
# print(my_pets)

# # ex. 1

# #.extend() method adds list 

# names = ["inky", "blinky", "pinky"]
# new = ["clyde", "new"]
# names.extend(new)
# print(names)

# ex. 2 

#names[2:4] = ("foo", "bar")
# print(names)

# ex. 3

names = ["inky", "blinky", "pinky", "clyde", "new"]
i = 0
while i < len(names):
    print(names)
    del names[i - 1]
print(names)