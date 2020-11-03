my_list = [10, 20, 30, 40, 50]
smallest = float("inf")

for num in my_list: 
    if num < smallest: 
        smallest = num

#easier built in method 
print(min(my_list))