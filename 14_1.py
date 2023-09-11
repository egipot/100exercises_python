#Question: 
# Complete the script so that it removes duplicate items from the list a .

a = ["1", 1, "1", 2]

#Expected output: 
# ['1', 2, 1] 

#egi solution
set_a = set(a)
print(list(set_a))
#or
b = ["1", 1, "1", 2]
print(list(set(b)))
 

#ardit solution
#Write a script that remove duplicates from a list
a = ["1", 1, "1", 2]
a = list(set(a))
print(a)

#If you want to keep the order, you need OrderedDict - this is the most effective
from collections import OrderedDict
a = [3, 2, "1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)

#third option, use append
c = [3, 2, "1", 1, "1", 2]
new_c = set(c)
newlist_c = []
i = 0
for i in range (len(c)):
    newlist_c.append(c[i])

print(list(set(newlist_c)))

###attempt do manually do the OrderedDict
d = [3, 4, 2, "1", 1, "1", 2]
new_d = set(d)
newlist_d = []
x = 0
for x in range (3):
    newlist_d.append(d[x])
    x = x + 1

print(list(set(newlist_d))) #fail :D read geeks for geeks