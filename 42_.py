#42 Iterating Multiple Sequences
#Print out in each line the sum of homologous items of the two consequences

a = [1, 2, 3]
b = (4, 5, 6)
bb = list(b)
#print(bb)

for i in range (0, len(a), 1):
    c = a[i] + bb[i]
    print(c)

#output:
# 5
# 7
# 9

#I just saw the hint: Check out zip

#ardit's solution
for i, j in zip(a, b):
    print(i + j)


help(zip)
# Help on class zip in module builtins:

# class zip(object)
#  |  zip(*iterables) --> A zip object yielding tuples until an input is exhausted.
#  |  
#  |     >>> list(zip('abcdefg', range(3), range(4)))
#  |     [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
#  |  
#  |  The zip object yields n-length tuples, where n is the number of iterables
#  |  passed as positional arguments to zip().  The i-th element in every tuple
#  |  comes from the i-th iterable argument to zip().  This continues until the
#  |  shortest argument is exhausted.
#  |  
#  |  Methods defined here:
#  |  
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |  
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |  
#  |  __next__(self, /)
#  |      Implement next(self).
#  |  
#  |  __reduce__(...)
# ...
#  |  
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.