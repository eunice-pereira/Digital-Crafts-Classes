num1 = [[2, 3, 5, 7, 8], [10, 3, 8, 9, 8]]
num2 = [[5, 10, 8, 4, 1], [45, 7, 0, 2, 4]]

# new = [sum(i) for i in zip(num[0], num[1])]

# new = []
# for num[0], num[1] in zip(num[0], num[1]): 
#     new.append(num[0] + num[1])

# print(new)

i = 0 
new = [] 
while i < len(num1): 
    j = 0 
    m = [] 
    while j < len(num1[i]): 
        m.append(num1[i][j] + num2[i][j]
        j += 1 
    new.append(m)
    i += 1
print(new)