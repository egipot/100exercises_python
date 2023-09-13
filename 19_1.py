#Question: Add a new pair of key (e.g. c ) and value (e.g. 3 ) to the dictionary and print out the new dictionary.

d = {"a": 1, "b": 2}

#Expected output: 
#  {'a': 1, 'c': 3, 'b': 2} 

#egi
print(type(d))
d["c"] = 3 #<class 'dict'>
print(d) #{'a': 1, 'b': 2, 'c': 3}

#Hint 1: Refer to key c  and use the assignment operator to assign a value to the key.
#Hint 2: Note that dictionaries are unordered collections, so don't worry about the order. It's always random. 