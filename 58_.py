#company1_exer58.json

# Exercise 58 - Add to JSON

# Question: Please download the json file in the attachment and use Python to add a new employee to the file's content 
# so that the file looks like in the expected output below.

# Expected output: 

# Hint 1: Open the file in "r+" mode.

# Hint 2: Create a dictionary out of the file content with json.loads , add the new pair of key and value to the dictionary,  
# do file.seek(0)  to put the cursor at the top of the file and then dump the dictionary to the opened file again.

import json

with open('company1.json', mode='r+') as f:
    #json.loads() converts a string into a dictionary object
    d = json.loads(f.read()) 
    d['employees'].append(dict(firstName= 'Albert', lastName= 'Bert'))
    f.seek(0)
    json.dump(d, f, sort_keys=True)
    f.truncate()

