# The person dictionary needs to have the keys, first_name, last_name, age, hair_color.
# Print each one of these key/values pairs without directly using the key's name as a string by using for loop.
# After each key value pair, print out a sentence using each one of the keys.

person = {
    "first_name" : "Eunice",
    "last_name" : "Pereira", 
    "age" : 33, 
    "hair_color" : "black"
}

for key in person: 
    print(key)
    print("Hello %s %s You are %s and have %s hair." % (person["first_name"], person["last_name"], person["age"], person["hair_color"]))

print(person["age"])