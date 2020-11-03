my_list = [2, 4, 6, 8, 0, 10, -5, -19]
factor = 4
new_list = []

for num in my_list: 
   new_list.append(num * factor)
print(new_list)

print([num * factor for num in my_list])