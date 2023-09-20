#39 Attribute Error
#The script is supposed to output the cosine of angle 1 radian, but instead, it is throwing an error.
#Please fix the code so that it prints out the expected output.

import math
#print (math.cosine(1))
print (math.cos(1)) #0.5403023058681398

#result: AttributeError: module 'math' has no attribute 'cosine'

#egi solution, change the "cosine" to "cos"

#hint: You could get a list of all available methods of the math module with dir(math) and see wheter cosine is there or not.

print(dir(math))
#['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']