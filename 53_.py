# Exercise 53 - Multilevel Dictionary

# Question: Print out the last name of the second employee.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                 {"firstName": "Anna", "lastName": "Smith"},
                 {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
           {"firstName": "Jessy", "lastName": "Petter"}]}
# Expected output: 
# Smith 

# Hint: Access employees  first, then the second item of employees  and then lastname .

#egi solution
#test codes
#print(d['employees']) 
#print(d['employees'][1])
print(d['employees'][1]['lastName'])

##############
#ardit answer:
# Exercise 53: Solution

# Exercise for reference: 

# Print out the last name of the second employee.

# d = {"employees":[{"firstName": "John", "lastName": "Doe"},
#                 {"firstName": "Anna", "lastName": "Smith"},
#                 {"firstName": "Peter", "lastName": "Jones"}],
# "owners":[{"firstName": "Jack", "lastName": "Petter"},
#           {"firstName": "Jessy", "lastName": "Petter"}]}
# Answer: 

# print(d['employees'][1]['lastName'])
# Explanation:

# d['employees']  returns this list:

# [{"firstName": "John", "lastName": "Doe"},
#  {"firstName": "Anna", "lastName": "Smith"},
#  {"firstName": "Peter", "lastName": "Jones"}]
# d['employees'][1]  returns the second item of the above list:

# {"firstName": "Anna", "lastName": "Smith"}
# And finally d['employees'][1]['lastName']  returns the value of lastName :

# Smith 
