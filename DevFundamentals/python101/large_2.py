# factor a number 
# give a number, print its factor

while True: 
    try:
        user_number = int(input("Enter number you would like to find a factor to:")

max_number = user_number + 1 
print("Here are your factors:")

for n in range(1, max_number): 
    factor = (user_number / n)
    if factor.is_integer():
        print(int(factor))
    n += 1