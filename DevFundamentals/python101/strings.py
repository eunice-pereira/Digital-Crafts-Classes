# concatenation 

print("Eunice " + "Pereira")

# escape strings 

haiku = "I like Python. \nand am excited to see \nwhat all I can create."
print(haiku)

# f-string syntax 

person = "classmate"
today = "Tuesday"
emotion = "grateful"

message = f'''
Hello {person}, 
I hope your {today} is going well.
I'm personally really {emotion}.
'''
print(message)

print(f"Hello {person}, \nI hope your {today} is going well.\nI'm personally really {emotion}.\n")

print("Hello %s,\nI hope your %s is going well.\nI'm personally really %s." % (person, today, emotion))
