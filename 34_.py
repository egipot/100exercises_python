# Local vs Global Variables
# Question: The following script throws a NameError  in the last line saying that c  is not defined. Please fix the function so that there is no error and the  last line can print out the value of c  (i.e. 1 ).

def foo():
    c = 1
    return c 
c = foo() #egi answer: assign the foo function's output to variable 'c'
print(c)
#Expected output = 1

#  File #"c:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - 100 Exercises\egi_solutions\34_.py", line 8, in <module>
#    print(c)
#NameError: name 'c' is not defined

# Hint 1: The reason for the error is that c  exists only inside the function namespace. In other words, c  is a local variable.
#Hint 2: Simply declare c  as a global variable inside the function.

##########
#ardit's answer:
def foo():
    global c
    c = 1 
    return c 
foo() 
print(c)
#Explanation: Adding global c  fixes the code. That line makes available name c  in the global namespace. Therefore,  print can access the variable c .