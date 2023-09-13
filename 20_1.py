#Question: Calculate the sum of all dictionary values.

d = {"a": 1, "b": 2, "c": 3}

#Expected output: 6
#Hint 1: First, use d.values()  to return an array with all dictionary values.
#Hint 2: Apply the sum()  function to the returned array.

#egi solution with help
values_list = d.values()
print(values_list) #dict_values([1, 2, 3])

def sum_result(values_list):
    sum = 0
    for i in values_list:
        sum +=i
    return sum   
print(sum_result(values_list)) #6

#short version ; also ardit's solution
print(sum(d.values())) #6

#Explanation: 
#d.values()  returns a list-like dict_values object,
#while the sum  function calculates the sum of the dict_values items.