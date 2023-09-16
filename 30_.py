# Arguments
# Question:  Why do you get an error, and how would you fix it?
# Hint: Always put non-default parameters first, followed by default ones.

def foo(b, a = 2):
    return a + b

#  File "c:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - 100 Exercises\egi_solutions\30_.py", line 3
#    def foo(a = 2, b):
#                    ^
#  SyntaxError: non-default argument follows default argument

print(foo(2))