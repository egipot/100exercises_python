#44 Letters Three by Three
#Create a script that generates a file where all letters of the English alphabet are listed three in each line. The inside of the text file would look like:
#abc
#def
#ghi
#and so on

#egi solution
from string import ascii_letters as strl  

with open('44_letters_egi.txt', 'w') as file:
    for letter1, letter2, letter3 in zip(strl[0::3], strl[1::3], strl[2::3]):
        file.write(letter1 + letter2 + letter3 + '\n')

#Hint: This is like the previous exercise, but with a different step.


#ardit solution
import string
letters = string.ascii_lowercase + ' '

slice1 = letters[0::3]
slice2 = letters[1::3]
slice3 = letters[2::3]

with open('44_letters_ardit.txt', 'w') as file:
    for s1, s2, s3 in zip(slice1, slice2, slice3):
        file.write(s1 + s2 + s3 + '\n')

