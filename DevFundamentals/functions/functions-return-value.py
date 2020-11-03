# returning is the value that a function sends out of the result when calling the func. 
# use results of a func to do something else (set as variable, argument, etc.)

def add_numbers(a,b): 
    result = a + b 
    return result 

value = add_numbers(1,3) / add_numbers(4,6)
print(value)

def mult_numbers(a,b):
    return a*b 
    
print(mult_numbers(5,6))