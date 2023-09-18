#37 Advanced Word Counter
#Create a function that takes a text file as input and returns the number of words contained in the text file. 
#Please take into consideration that a comma can separate some words with no space. 
#For example, "Hi, it's me." would need to be counted as three words. 
#For your convenience, you can use the text file in the attachment.

#Hint: You could replace all commas with spaces.

with open("C:\\Users\\GayCalaranan.000\\Documents\\Programming\\Udemy - Python - 100 Exercises\\egi_solutions\\words1.txt", 'r') as my_file:
    my_words = my_file.read()
    my_words.replace(',', ' ')
    word = my_words.split(' ')
    print(len(word))

def count_words (sentence):
    sentence.replace(',', ' ')
    count = sentence.split(' ')
    print(len(count))

count_words("Hi! It's me!")

#ardit's answer
def count_words(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    text = text.replace(",", " ")
    string_list = text.split(" ")
    return len(string_list)

print(count_words("words2.text"))