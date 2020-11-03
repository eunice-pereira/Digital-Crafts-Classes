x = 10 

def add_to_x(a): 
    return x + a

def add_two_numbers(a,b): 
    c = a + b 
    return c 

def repeat_stuff(): 
    x = 10 
    def update_x(): 
        return x + x 
    while x < 100: 
        x = update_x()
        print(x)

print(add_to_x(12))
print(add_to_x(33))

print(add_two_numbers(10,20))
#print(c)

repeat_stuff()