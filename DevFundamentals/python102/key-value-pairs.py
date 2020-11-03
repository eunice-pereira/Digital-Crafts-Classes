# dictionary is a data type that is a grouping of data and uses keys to point to a value 
# keys are strings, int, or any variety type that will allow dev to access a value 

# in python, key value pairs are dictionaries 
# dictionaries can have multiple data types as values 

movie = {
    "name": "Star Wars", 
    "episode": 4, 
    "year": "1977", 
    "villains": ["Vader", "Tarkin"],
    "heros": ["Luke", "Leia", "Han"]
}
# print from dictionary 
print(movie["name"])

#assing to a variable 
episode_num = movie["episode"]

#accessing value from array in dictionary 
print(movie["heros"][1]) # leia

# check for existence 
if key in movie: 
    print(movie[key])
else: 
    print("item not found")

# add to current string 
movie["name"] = movie["name"] + "- A new Hope"

#adding a new item 
movie["ships"] = ["Falcon", "Star Destroyer", "Death Star"]

# add to an element inside a list 
movie["heros"].append("Chewbacca")