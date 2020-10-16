# print a box 

w = int(input("Enter box width:"))
h = int(input("Enter box height:"))

# rows

row = '*' * w
empty = w - 2
middle = '*' + ' ' * empty + '*'

print(row + '\n' + (middle + '\n') * h + row) 

