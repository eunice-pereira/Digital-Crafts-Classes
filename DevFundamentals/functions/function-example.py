# printing to-dos with function 
todos = []

main_menu = '''
Choose an action: 
P: Print your to-do list 
A: Add a to-do item 
R: Replace a to-do item 
C: Complete a to-do item 
(or press Enter to exit the program)
'''

def print_todos(): 
    #prints curent list of to-do items 
    print("\n\n\nTo do:")
    print("==================")
    count = 1 
    for todo in todos: 
        print("%d: %s" % (count, todo))
        count += 1 
    
choice = input(main_menu)
choice = choice.upper() #simplifies our if-conditions

while len(choice) > 0: 
    if choice == "P": 
        print_todos()
    elif choice == "A": 
        new_todo = input("What do you need to do?")
        if len(new_todo) > 0: 
            todos.append(new_todo)
    elif choice == "R": 
        print_todos()

        which_index = input("Which to-do number?")
        try: 
            which_index = int(which_index)
            which_index -= 1 #convert from human-readable to 0-based index 

            if which_index >= 0 and which_index < len(todos): 
                new_todo = input("What do you need to do?")
                todos[which_index] = new_todo
        except ValueError: 
                print("\n\n***Please enter a number.***")
    elif choice == "C": 
        print_todos()

        which_index = input("Which to-do number?")
        try: 
            which_index = int(which_index)
            which_index -= 1 

            if which_index >= 0 and which_index < len(todos):
                completed_todo = todos[which_index]
                del todos[which_index]
                print("%s has been marked complete!" % completed_todo)
        except ValueError: 
            print("\n\n***Please enter a number.***")
    else: 
        print("\n\n***Please enter a valid menu option.***")
    
    choice = input(main_menu)
    choice = choice.upper()

print("Have a nice day!")