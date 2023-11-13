# Exercise 51 - EOF

# Question: The code produces an error. Please understand the error and try to fix it.

#egi answer: this code has missing )
#print(type("Hey".replace("ey","i")[-1]) 

print(type("Hey".replace("ey","i")[-1]) )

#Hint: An open bracket always needs a closing bracket.


##################
# #ardit answer
# Exercise for reference: 

# The code produces an error. Please understand the error and try to fix it

# print(type("Hey".replace("ey","i")[-1])
# Answer: 

# print(type("Hey".replace("ey","i")[-1]))
# Explanation:

# This code produces a SyntaxError: unexpected EOF while parsing which means that Python found an unexpected End Of File while parsing. The reason for an unexpected end of file is there's a missing closing bracket at the end of the script. So, adding a closing bracket at the end of the file fixes the code.