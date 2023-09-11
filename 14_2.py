# Complete the script so that it removes duplicate items from the list a .

a = ["a", "1", 1, "1", 2]

#Expected output: 
# ['1', 2, 1] 

def unsorting_func(a):
    unsorted_a = []
    for i in a : #for as long as function goes to each element in order,
        if i not in unsorted_a: #if not yet stored in the list "unsorted_a"
            unsorted_a.append(i) #append the element in the list "unsorted_a"
    return unsorted_a

print(unsorting_func(a)) #['a', '1', 1, 2]