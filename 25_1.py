#Create a script that prints out letters of English alphabet from a to z

#answer from https://datagy.io/python-list-alphabet/

#solution1: use the string module
import string
print(f'#1a result: {string.ascii_letters}') #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(f'#1b result: {string.ascii_lowercase}') #abcdefghijklmnopqrstuvwxyz
print(f'#1c result: {string.ascii_uppercase}') #ABCDEFGHIJKLMNOPQRSTUVWXYZ
#1a result: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
#1b result: abcdefghijklmnopqrstuvwxyz
#1c result: ABCDEFGHIJKLMNOPQRSTUVWXYZ

#solution2: use of string function and pass as a list of characters []
print(f'#2 result: {list(string.ascii_letters)}')
#2 result: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#solution3: use of chr function which converts an integer value to its corresponding Unicode value
alphabet = []
for i in range (97, 123):
    alphabet.append(chr(i)) #chr=character 

print(f'#3 result: {alphabet}')
#3 result: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#solution4: use of ord function which converts a Unicode value into its integer representation + FOR loop
alphabet2 = []
start = ord('a') #return the unicode code of a one-character string
end = ord('z') #return the unicode code of a one-character string
for x in range ((end+1)-start):
    alphabet2.append(chr(start + x))
print(start, end) #97 122
print(f'#4 result: {alphabet2}')
#4 result: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#solution5: list comprehension
alphabet3 = [chr(value) for value in range (97, 123)]
print(f'#5 result: {alphabet3}')
#5 result: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#solution6: map function
alphabet4 = list(map(chr, range(97, 123)))
print(f'#6 result: {alphabet4}')
#6 result: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']