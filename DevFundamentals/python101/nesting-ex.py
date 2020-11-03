pet_name = input("What is your pet's name?:\n") 
length = int(len(pet_name))

if length > 3 and pet_name != "Shadow": 
    print(f"Awww, sweet {pet_name}!")
    if pet_name == "Shadow": 
        print("El Gato Diablo!")
    if pet_name == "Daisy":
        print("Good Dog!")
else length < 3: 
    print("Name length is too short.")