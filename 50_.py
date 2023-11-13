# Exercise 50 - Text Input

# Question: The code produces an error. Please understand the error and try to fix it

#age = input("What's your age? ") --> the entered number will be considered a string. String cannot be used immediately in numerical operations. Must be converted first.

#egi solution 1: PREFERRED
age = int(input("What's your age? "))
age_last_year = age - 1

#egi solution 2: less preferrred
# age = input("What's your age? ")
# age_last_year = int(age) - 1  


print("Last year you were %s." % age_last_year)
#Note: Please use raw_input instead of input if you are on Python 2. For Python 3 input is fine.
# Hint 1: The input  function always returns a string type.
# Hint 2: Convert the input to an integer with int .

##############
# ardit answer:
# Exercise for reference: 

# The code produces an error. Please understand the error and try to fix it

# age = input("What's your age? ")
# age_last_year = age - 1
# print("Last year you were %s." % age_last_year)
# Answer 1: 

# age = int(input("What's your age? "))
# age_last_year = age - 1
# print("Last year you were %s." % age_last_year)
# Explanation 1:

# As you can see, we applied an int  function to the input  function. That converts user input to an integer right away.

# Answer 2: 

# age = input("What's your age? ")
# age_last_year = int(age) - 1
# print("Last year you were %s." % age_last_year)
# Explanation 2:

# In this alternative solution, we applied the int  function in the line where the math operation occurs. This could be useful if you intend to use the user input value as a string in other parts of your script, so you don't want to convert it to an integer directly.