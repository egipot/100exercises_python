# Exercise 68 - User Friendly Translator

# Question: Create an English to Portuguese translation program.

# The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source. 
# Also, return the message, "We couldn't find that word!" when the user enters a word that is not in the dictionary. Also, make the program non-case-sensitive, meaning that, for example, both earth and Earth should return the translation correctly for that word.

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

# Expected output: 

# Enter word: hello
# We couldn't find that word!

def translator():
    try:
        word = input('Enter a word to translate: ')
        print(d[word.lower()])
    except:
        print('We couldn\'t find that word!')

translator()

# Enter a word to translate: Earth
# terra

# Enter a word to translate: hello
# We couldn't find that word!

# Enter a word to translate: WEAther
# clima

#####
#ardit answer:
# d = dict(weather = "clima", earth = "terra", rain = "chuva")
# def vocabulary(word):
#     try:
#         return d[word]
#     except KeyError:
#         return "We couldn't find that word!"
 
# word = input("Enter word: ").lower()
# print(vocabulary(word))