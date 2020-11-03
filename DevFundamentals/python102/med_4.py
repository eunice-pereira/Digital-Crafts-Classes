num = [1, 2, 8, 8, 5, 6]

new = []
for i in num: 
    if i not in new: 
        new.append(i)
print(new)

# not in evaluates to true if it does not find a variable in specified sequence

# method 2 

print(list(set(my_list)))