#Create a dictionary of keys a, b, c, where each key has as value a list from 1 to 10, 11 to 20, and 21 to 30 respectively and print out.

#Hint: Use a range function to create the lists

#egi
dict1 = {"a": list(range(1,11)), "b": list(range(11, 21)), "c": list(range (21,31))} 
print(dict1)

print(list(range(1,11))) #{'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}

sum_A = dict1["a"]
print(sum(sum_A))



#Ardit answer: 

from pprint import pprint
 
d_ardit_solution = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
pprint(d_ardit_solution)

#Explanation: 
#We're using ranges here to construct the lists. 
#We're also using the built-in Python pprint  module, which is used to print out well-formatted views of datatypes in Python.
#{'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
# 'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
# 'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}