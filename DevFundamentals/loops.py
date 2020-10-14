# i = 2
# max_num = 20
# increment = 2
# while i < max_num:
#     print(i)
#     i += increment #everything in this code block will run as condition is met (i < 10)

# i = 1 
# while i <= 10: 
#     print(i)
#     i += 1

# i = 10 
# while i > 0: 
#     print(i)
#     i -= 1

username = "epereira"
password = "123"
attempt = 0 
remain = 3

while attempt < 3: 
    user_input = input("Username:")
    pass_input = input("Password:")

    if user_input == username and pass_input == password:
        print("Welcome!")
        attempt = 4
    else: 
        attempt += 1
        remain -= 1

        if attempt < 3: 
            print(f"Please try again. You have {remain} attempts left.")
        else: 
            print("You have reached the maximum number of attempts.")
            