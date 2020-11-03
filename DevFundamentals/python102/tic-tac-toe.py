# tic tac toe 

size = 3 
board = [] # start with empty list 

for y in range(size): 
    # each element in board will also be a list 
    board.append([])
    for x in range(size): 
        # fill our inner lists with coordinates 
        board[y].append("[%d][%d]" % (y,x))

# print board as a grid 
for row in board: 
    for column in row: 
        print("%s  " % column, end='')
    print("\n")

print("\n\nPlayer X is moving.\n\n")
board[0][2] = "     X"

# print the board as a grid 
for row in board: 
    for column in row: 
        print("%s " % column, end=" ")
    print("\n")

print("\n\nPlayer O is moving.\n\n")
board[1][1] = "   O     "

for row in board: 
    for column in row: 
        print("%s " % column, end=" ")
    print("\n")

print("\n\nPlayer X is moving.\n\n")
board[1][2] = "  X"

for row in board: 
    for column in row: 
        print("%s " % column, end=" ")
    print("\n")

print("\n\nPlayer O is moving.\n\n")
board[2][1] = "   O     "

for row in board: 
    for column in row: 
        print("%s " % column, end=" ")
    print("\n")

print("\n\nPlayer x is moving.\n\n")
board[2][2] = "  X     "

for row in board: 
    for column in row: 
        print("%s " % column, end=" ")
    print("\n")

print("\n\nPlayer X wins!\n\n")