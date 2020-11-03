# ex. 1 
shopping_list = [
    ['Corn','Potatoes','Tomatoes'],
    ['milk','eggs','cheese','yogurt'],
    ['frozen pizza','popsicle']
]

food = ["veggies", "dairy", "desert"]

# for i in food: 
#     print(i)

# ex. 2 
# Using the code from the previous exercise, 
# have each grouping have a title with the number in the title 
# and each item of the list have a number in front of the item.


for i in food: 
    i = 0 
    print(f"{i + 1}. {food}")
    for food in shopping_list[i]: 
        j = 0
        print(f"{j + 1}. {food}")
    i += 1
        