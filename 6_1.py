#Complete the script so that it prints out a list containing letters d, e, f.
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

#egi solution: 
print(f"{letters[3]}", f", {letters[4]}", f", {letters[5]}")
#output: d , e , f

#ardit note: Slicing is upper-bound exclusive
#ardit solution:
print(letters[3:6])
#output ['d', 'e', 'f']
#ardit explanation: 
#  d  has an index of 3  here, 
#  e  has an index of 4 , and 
#  f  has an index of 5, 
# but since the slicing syntax is upper-bound exclusive, we need to pass 6  as the upper bound.
