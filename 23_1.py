#Question: Access the third value of key b  from the dictionary.

from pprint import pprint
 
d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

#Expected output: 13  

#egipot
list_b = d["b"]
print(list_b[2])

#Hint: You need square brackets after square brackets here.

#Ardit answer:
pprint(d["b"][2])