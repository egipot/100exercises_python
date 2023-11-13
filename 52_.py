# Exercise 52 - String Formatting
# Question: The code is supposed to ask the user to enter their name and surname, and then it prints out those user submitted values. 
# Instead, the code throws a TypeError. Please fix it so that the expected output is printed out.

firstname = input("Enter first name: ")
secondname = input("Enter second name: ")

#print("Your first name is %s and your second name is %s" % firstname, secondname)
#^This line results to an error:
# Traceback (most recent call last):
#   File "c:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - 100 Exercises\egi_solutions\52_.py", line 7, in <module>
#     print("Your first name is %s and your second name is %s" % firstname, secondname)
# TypeError: not enough arguments for format string

# Expected output: 
# Your first name is John and your second name is Smith 
# Hint: Python expects a tuple after %.

#egi solution:
print(f'Your first name is {firstname} and your second name is {secondname}')

################################
#ardit solution:
# Answer: 
# firstname = input("Enter first name: ")
# secondname = input("Enter second name: ")
# print("Your first name is %s and your second name is %s" % (firstname, secondname))
# Explanation:

# Each of the %s  placeholders expect one value after %  to be replaced with, but you need to pass these values inside a tuple. So, putting variables firstname  and secondname  inside a tuple fixes the code.