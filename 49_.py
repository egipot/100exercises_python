# Exercise 49 - Pass

# Question: The code is supposed to get some input from the user, but instead, it produces an error. Please try to understand the error and then fix it.

# pass = input("Please enter your password: ") 

# Note: Please use raw_input  instead of input if you are on Python 2. For Python 3 input  is fine.

#When run, this outputs:
#     pass = input("Please enter your password: ") 
#          ^
# SyntaxError: invalid syntax

#egi solution: DO NOT USE a reserved word e.g. pass
text = input("Please enter your password: ") 

#Hint: You cannot use reserved keywords for variable names.

# Exercise for reference: 

# The code is supposed to get some input from the user, but instead, it produces an error. Please try to understand the error and then fix it.

# pass = input("Please enter your password: ") 

# Answer: 

# pass1 = input("Please enter your password: ") 

# Explanation:

# There was a SyntaxError  error because the syntax to name the variable was wrong since pass  is a reserved keyword in Python. However, you can solve that by adding a number to the name or simply choosing another variable name.