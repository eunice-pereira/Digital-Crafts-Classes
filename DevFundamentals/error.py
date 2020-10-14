my_num = input("Give me a number:")

try: 
    my_num = int(my_num)
    print(100 / my_num)
except ZeroDivisionError:
    print("You tried to divide by 0")
except TypeError:
    print("You did something wrong with the type")
except ValueError: 
    print("You didn't give me a number:")

