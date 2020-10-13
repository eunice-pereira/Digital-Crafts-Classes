# booleans are data types

print(1 == 2) 
print(1 < 2)
print(1 > 2)
print(1 >= 1)
print(1 <= 2)
print(1 != 1)

# if-statements execute code block if condition is true 
# code block is section of code that is executed in sequence 

if 1 < 3: 
    print("This will not be printed")

# This wil not print/execute because it is false 
if 0: 
    print("0 is a false statement ")

if 1: 
    print("1 is a truth statement")

# Falsey statements 
None 
False 
0 
" "     # empty string 
[]      # empty array in Python
{}      # empty brackets in Python

# Excercise 

print(1 == 3)
print(4 <= 4)
print("a" == "a")
print(10 > 11)
print("b" > "c")

my_number = 33
print(50 == my_number)
print(100 <= my_number)
print(my_number >= 100)

name = "Eunice"

if name == "Eunice": 
    print("YES these strings are the same!")

if name != "eunice": 
    print("NO these strings are different!")