#Generate a list from 1-20 without typing manually

#egi solution
myset = set()
num = 1
max = 20

for num in range (max):
    num = num + 1
    myset.add(num)

print(list(myset))


#ardit solution
#Create a script that generates a list of numbers from 1 to 20. Do not create a list manually.
my_range = range(1, 21)
print(list(my_range))