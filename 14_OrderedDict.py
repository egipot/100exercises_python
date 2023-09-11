#example 1:
d = {
    'de': 'Germany', 
    'sk': 'Slovakia',
    'hu': 'Hungary',
    'pl': 'Poland',
    'bg': 'Bulgaria',
    'ph': 'Philippines'
}

d_sorted = {k: v for k, v in sorted (d.items(), key=lambda x:x[1])}
print(d_sorted)

#example2: #fail - output is still sorted; storing for educational purposes
list_A = [3, 4, 2, "1", 1, "1", 1, "1", 5]
i = 0
def Convert(list_A):
    dict_A = {i: list_A[i] for i in range (len(list_A))}
    #i = i + 1
    return dict_A

set_A = Convert(list_A)
print(set_A)  # {0: 3, 1: 4, 2: 2, 3: '1', 4: 1, 5: '1', 6: 1, 7: '1', 8: 5}
print(type(set_A)) # <class 'dict'>
print(set_A.values()) # dict_values([3, 4, 2, '1', 1, '1', 1, '1', 5])
print(list(set_A.values())) # [3, 4, 2, '1', 1, '1', 1, '1', 5]
print(set(list(set_A.values()))) # {1, 2, 3, 4, 5, '1'}
#print(set(list_A))      # {1, 2, 3, 4, '1'}
#print(dict.fromkeys(list_A)) # {3: None, 4: None, 2: None, '1': None, 1: None, 5: None}


#example3: SUCCESS!!!!
#from : https://stackoverflow.com/questions/52090334/printing-elements-of-a-set-in-python
#Python set is unordered collections of unique elements
e = [3, 4, 2, "1", 1, "1", 1, "1", 5]

def removeDups(e):
    unsorted_e = []
    for i in e:
        if i not in unsorted_e:
            unsorted_e.append(i)
    return unsorted_e

print(removeDups(e)) # [3, 4, 2, '1', 1]