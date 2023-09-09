#Generate a list from 1-20 without typing manually

#egi solution
max = 20
my_set = set()

for num in range (max):
    num = num + 1
    my_set.add (num)
print(my_set) #output {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
print(list(my_set)) #workaround: convert the set to list :D 
#output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]



#ardit solution
#Create a script that generates a list of numbers from 1 to 20. Do not create a list manually.
my_range = range(1, 21)
print(list(my_range))
#output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#Explanation: 
#range()  is a Python built-in function that generates a range of integers. 
# However, range()  creates a Python range object. 
# To get a real list object, you need to use the list() function to convert the range object into a list object.

#lesson learned: my solution returned a set, while ardit's solution returned a list.
#{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]