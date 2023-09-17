#35 Create a function that takes any string as input and returns the number of words for that string.
#Hint1: Convert the string to a lost with split
#Hint2: Once you do string.split(" "), then apply the len method to the produced list --> I figured this out before reading the hint

string = input('Enter a list of words: ')
string_list = string.split(sep=" ")
print(len(string_list))



#ardit's answer:
def count_words(strng):
    strng_list = strng.split()
    return len(strng_list)

print(count_words('Hey there it\'s me!'))