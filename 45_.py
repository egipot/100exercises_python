#45 One File per Letter
#Please create a script that generates 26 text files named a.txt, b.txt, and so on up to z.txt.
#Each file should contain a letter reflecting its filename. 
#So a.txt will contain a letter a, b.txt will contain letter b and so on

#Hint: Start iterating with a for loop and create a file in each iteration.

#egi solution:
from string import ascii_lowercase as strlw

for letter in strlw:
    #with open('{letter}.txt', 'w') as file: This outputs one text file: {letter}.txt having 'z' as content
    with open(letter + ".txt", "w") as file: #This creates all the 26 files in the same folder; hence, not organized. Ardit's solution is better
        file.write(letter)


#ardit's solution
import string, os

if not os.path.exists('44_letters_ardit'):
    os.makedirs('44_letters_ardit')
for letter in string.ascii_lowercase:
    with open('44_letters_ardit/' + letter + '.txt', 'w') as file:
        file.write(letter + '\n')

