# multiply vectors 

num1 = [2, 4, 5] 
num2 = [4, 12, 30]
product = []
i = 0 

# method 1 using while loop 
while i < len(num1): 
    product.append(num1[i] * num2[i])
    i += 1
print(product)

# method 2 using for loop 
for num1, num2 in zip(num1, num2): 
    product.append(num1 * num2)
print(product)

# method 3 advanced method
print([num * num2[idx] for idx, num in enumerate(num1)])