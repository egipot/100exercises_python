# Exercise 67 - Advanced Translator

# Question: Create an English to Portuguese translation program.

# The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source. In addition, try to return the message, "We couldn't find that word!" when the user enters a word that is not in the dictionary.

# d = dict(weather = "clima", earth = "terra", rain = "chuva") 

# Expected output: 

# Enter word: hello
# That word doesn't exist!

# #egi solution:
def translator():
    try:
        word = input('Enter a word to translate: ')
        print(d[word])
    except:
        print('That word doesn\'t exist!')

translator()



#ardit solution:
# d = dict(weather = "clima", earth = "terra", rain = "chuva")
# def vocabulary(word):
#     try:
#         return d[word]
#     except KeyError:
#         return 'That doesn\'t exist!'

# word = input("Enter word: ")
# print(vocabulary(word))
