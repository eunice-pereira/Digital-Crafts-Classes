# Create a program that does the same thing as above, 
# but the function only accepts a single argument to get the same results.
# will need to use a datatype other than a string in the argument.

# def movie(movie_item): 
#     title = movie_item[0]
#     genre = movie_item[1]
#     year = movie_item[2]

#     print(f'''
#     1. Title : {title}
#     2. Genre : {genre}
#     3. Year : {year}
#     ''')

# movie(["Training Day", "Action", 2001])

# another method using for loop

def movie(movie_item): 
    idx = 1
    for item in movie_item:
        print(f"{idx}. {item} : {movie_item[item]}")
        idx += 1
movie({"Genre" : "horror", "title": "beach", "year":2020})