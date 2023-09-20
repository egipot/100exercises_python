#41 Lettters in File
#Create a script that generates a text file with all letters of the English alphabet inside it, one letter per line.

#Hint: You need to open a file in write mode, iterate through a list of letters and use write method in each iteration.

import string

#letters = string.ascii_letters
with open ('letters_egi.txt', 'w') as f:
    for letter in string.ascii_letters:
        f.write(letter)
        f.write('\n')

#Reference: https://www.pythontutorial.net/python-basics/python-write-text-file/

#ardit's answer:
with open ('letters_ardit.txt', 'w') as file:
    for letter in string.ascii_lowercase:
        file.write(letter + '\n')
