#Exercise 24 - Iterate Dictionary

#Question: Please complete the script so that it prints out the expected output.

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

#Expected output: 
#b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
#a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Hint: Iterate through the d.items()  (Python 3) or d.iteritems()  (Python 2) with a for loop.

#egi
from pprint import pprint
pprint(d)

for k, v in d.items():
    print(f'{k} has value {d[k]}')

#result: 
#a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


#Ardit answer:
for key, value in d.items():
    print(key, "has value", value)
#result is the same
#a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]