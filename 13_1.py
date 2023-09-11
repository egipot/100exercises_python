#Question: 
#Complete the script, so it generates the expected output using my_range as input data. 
# Please note that the items of the expected list output are all strings.

my_range = range(1, 21)
my_range2 = range(1, 21)

#Expected output: 
#['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']  

#egi solution :) I did not see at first the "map" function hint
str_range = []
for i in my_range:
    my_range = str(i)
    str_range.append(my_range)
print(str_range)

#egi attempt2 using the "map" function
str_range2 = list(map(str, my_range2))
print(str_range2)
#['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

#ardit solution
#Create a script that converts all items of the range to strings
my_range3 = range(1, 21)
print(list(map(str, my_range3)))
#['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
