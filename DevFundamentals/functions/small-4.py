# Write a function that accepts a number as an argument and returns a Boolean value. 
# Return True if the number is even; return False if it is not even.

def is_even(number): 
    if number % 2 == 0: 
        return True 
    else: 
        return False

print(is_even(5))