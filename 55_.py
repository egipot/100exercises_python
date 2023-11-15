# Exercise 55 - Adding to Multilevel Dictionaries

# Question: Please add a new employee to the dictionary.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

# Expected output: 
# {'employees': [{'firstName': 'John', 'lastName': 'Doe'},
#                {'firstName': 'Anna', 'lastName': 'Smith'},
#                {'firstName': 'Peter', 'lastName': 'Jones'},
#                {'firstName': 'Albert', 'lastName': 'Bert'}],
#  'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
#             {'firstName': 'Jessy', 'lastName': 'Petter'}]}


#Hint: Access employees and use append to apply a new dict with keys firstName, and lastName  and the new values for those keys.

d['employees'].append({'firstName': 'Albert', 'lastName': 'Bert'})
print(d)
print(type(d))

################################
#ardit Answer: 

#d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))
# print(type(d))
# Explanation:

# d['employees']  returns this list:
# [{"firstName": "John", "lastName": "Doe"},
#  {"firstName": "Anna", "lastName": "Smith"},
#  {"firstName": "Peter", "lastName": "Jones"}]
# Then d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))  appends a new item to the list. This item happens to be a new dictionary.
