# Exercise 57 - JSON to Dictionary

# Question: Please download the file in the attachment and use Python to print out its content.
# C:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - 100 Exercises\company1.json

#egi solultion
import json

with open('company1.json', mode='r') as data:
    print(json.load(data))
    


# Expected output: 

# {'employees': [{'firstName': 'John', 'lastName': 'Doe'},
#                {'firstName': 'Anna', 'lastName': 'Smith'},
#                {'firstName': 'Peter', 'lastName': 'Jones'}],
#  'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
#             {'firstName': 'Jessy', 'lastName': 'Petter'}]}

# Hint: This can be done through the json  and the pprint  built-in modules.