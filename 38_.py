#38 Name error
#The following code is supposed to print out the square root of 9, but it throws an error instead because another line before that is missing. 
#Please fix the script so that it prints out the square root of 9.
import math #egi solution, add import math. Without this line, the result is "NameError: name 'math' is not defined"
math.sqrt(9)

#Hint: math is a built-in Python module containing various math methods

#Ardit explanation: Since you get the error that math is not defined, that means math is not in the default namespace.
#With some internet search, you could easily find out that math is a module, so you simply need to do "import math"