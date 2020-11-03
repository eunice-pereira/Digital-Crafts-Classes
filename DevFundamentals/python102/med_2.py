num1 = [[2, -2], [5, 3]]
num2 = [[1,4], [3,2]]

# new_matrix = 

# for num, num2 in zip(num, num2: 
#     #new.append(num[0] + num[1])

# # new = [sum(i) for i in zip(num, num2)]

# print(new)

new_matrix = []
for i in range(len(num1)): 
    m = [] 
    for j in range(len(num1[i])):
        m.append(num1[i][j] + num2[i][j])
    new_matrix.append(m)
print(new_matrix)