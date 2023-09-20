#40 TypeError
#Please try to guess what is missing in the following code and add the missing part so that the code works fine.

import math
#print(math.pow(2))
#egi note: missing argument, should be (x, y)
print(math.pow(2,2)) #4.0

#when run: "TypeError: pow expected 2 arguments, got 1"
#hint: Simply pass two arguments

print(help(math.pow))
# Help on built-in function pow in module math:

# pow(x, y, /)
#     Return x**y (x to the power of y).