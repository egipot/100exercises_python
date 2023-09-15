#Question: Make a script that prints out numbers from 1 to 10
#Hint: Iterate through a range object.

#egi
num_list = list(range(1,11))
num_iter = []
for x in num_list:
    print(f'{x}')

#Ardit answer:
for i in range(1,11):
    print(i)

#Explanation: 
#A for  loop is used to repeat an action (i.e. print ) until the iterating sequence (i.e. range ) is consumed. 
#In our case, it would print all items of the range one by one.