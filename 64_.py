#Exercise 64
#The following code prints Hello, checks if 2 is greater than 1, then breaks the loop because 2 is actually greater than 1.
#Therefore Hi is ot printed out. Please replace break with something else so that Hello and Hi are printed out repeatedly.

while True:
    print('Hello')
    if 2 > 1:
        break
    print('Hi') 

#egi answer:
while True:
    print('Hello')
    if 2 > 1:
        pass
    print('Hi') 

#correct answer :) 