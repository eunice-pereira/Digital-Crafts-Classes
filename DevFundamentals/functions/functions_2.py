# Create a program that has a function that will accept 3 arguments as 
# title, genre, year and then print out the values in list format.

def movies(title, genre, year): 
    print(f'''
    1. Title : {title}
    2. Genre : {genre}
    3. Year : {year}
    ''')

movies("Training Day", "Action", 2001)
