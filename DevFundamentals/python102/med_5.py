# Given a paragraph of text as a String, print the paragraph in leetspeak.

# To translate a String to leetspeak, 
# you need to replace make the following character replacements 
# (treat all input characters as uppercase):

my_string = "TEST SENTENCE"

replacements = [('A','4'), ('E', '3'), ('G','6'), ('I','1'),('O','0'), ('S','5'), ('T','7')]
new_string = my_string

for letter, number in replacements: 
    new_string = new_string.replace(letter,number)

print(new_string)
