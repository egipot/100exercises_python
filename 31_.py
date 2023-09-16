# Function Blueprint:
# Question:  Why is there an error in the code, and how would you fix it?
# Hint: A function is called using bracket notation ().

def foo (a = 1, b = 2):
    return a + b

###
# I added these two lines to check value
print(foo())    # 3 which is an integer 
print(foo)      # <function foo at 0x000001C3B3B229D0> which represent the memory where this function is allocated in
###

x = foo() - 1   

print(x)        #2

# results to:
#  File "c:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - 100 Exercises\egi_solutions\31_.py", line 7, in <module>
#    x = foo -1
#TypeError: unsupported operand type(s) for -: 'function' and 'int'

#Solution is to add '()' when calling the function --> x = foo() - 1 

