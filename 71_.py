# Exercise 71 - Letter Counter

# Question: Count the number of "a" characters in this text file: http://www.pythonhow.com/data/universe.txt (bad link, use the previous link instead 'https://pythonhow.com/media/data/universe.txt')
# Expected output: 
# 47


#egi answer before seeing the hint
import requests

file = requests.get('https://pythonhow.com/media/data/universe.txt')
file_content = str(file.content)
counter_a = 0

for t in file_content:
    if t == 'a':
        counter_a += 1
    else:
        pass

print(counter_a) #47
#print(file_content)


#egi answer after seeing the Hint
#Hint: Use the requests  library to load the text file content in Python and then use the count  method.

print(file_content.count('a')) #47