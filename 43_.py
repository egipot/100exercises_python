#43 Letters Two by Two
#Create a script that generates a file where all letters of the English alphabet are listed two in each line. The inside of the text file would look like:
#ab
#cd
#ef
#Hint1: Use the zip function to iterate through two slices of the letters sequence
#Hint2: One slice would be string.ascii_lowercase[0::2] and the other string.ascii_letters[1::2]

#egi answer
import string
# x = 0
# a = string.ascii_lowercase[0::2]
# b = string.ascii_letters[1::2]

# with open('43_letters_egi.txt', 'w') as file:
#     for a, b in zip(a, b):
#         file.write(a + b +'\n')


#ardit answer
with open ('43_letters_ardit.txt', 'w') as file:
    for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_letters[1::2]):
        file.write(letter1 + letter2 + '\n')

