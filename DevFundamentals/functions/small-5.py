# Write an is_odd function that uses your is_even function to determine if a number is odd. 
# (That is, do not do the calculation - call a function that does the calculation.)

def is_even(number): 
    if number % 2 == 0:
        return True 
    else: 
        return False

def is_odd(number): 
    if is_even return True: 
        print(f"{number} is odd")