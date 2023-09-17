#36 Word counter from a text file
#Please download the words1.txt from the attachment and then create a Python function that takes a text file as input and returns the number of words contained in the text file.

#Expected output = 10

#Hint: Create a function that takes a file path as input, reads the file, splits the content, and counts the items of the split output.


# with open("C:\\Users\\GayCalaranan.000\\Documents\\Programming\\Udemy - Python - 100 Exercises\\egi_solutions\\words1.txt", 'r') as my_File:
#     my_File_list = [word.strip(' ') for word in my_File.read().split()]
# print(len(my_File_list)) #10


# with open(r"C:\Users\GayCalaranan.000\\Documents\Programming\Udemy - Python - 100 Exercises\egi_solutions\words1.txt", 'r') as my_File:
#     my_File_list = [word.strip(' ') for word in my_File.read().split()]
# print(len(my_File_list)) #10

#References:
#https://www.programiz.com/python-programming/file-operation
#https://stackoverflow.com/questions/33007218/how-to-use-strip-in-python




#ardits's answer
def count_words(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)
    
#added this line to call the function
print(count_words("c:\\Users\\GayCalaranan.000\\Documents\\Programming\\Udemy - Python - 100 Exercises\\egi_solutions\\words1.txt"))
    
