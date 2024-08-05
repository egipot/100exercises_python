#96 File Writer

# Create a program that asks the user to submit text repeatedly
# The program closes when the user submits CLOSE

# So the user enters hey there you and so on and so forth. 
# And the program closes when the user enters CLOSE with capital letters.
#At that point a text file has been created.
#This one here, data.txt where you have all the user submitted values one in each line.

# Hint: Consider using break in the while loop.


def file_writer():
    #list that stores the text input
    result =  open('96_data_output.txt', 'a+')

    #loop until user enters CLOSE (case-sensitive)
    while True:
        userinput = input("Submit a text: ") 
        if userinput == 'CLOSE':
            break
        else:
            result.write(userinput + '\n')

file_writer()

#PS C:\...\Udemy - Python - 100 Exercises\egi_solutions\96_.py"
# Submit a text: qwerty
# Submit a text: asdf
# Submit a text: zxcv
# Submit a text: close
# Submit a text: CLOSE
#PS C:\...\Udemy - Python - 100 Exercises\egi_solutions\96_.py"
# Submit a text: poiu
# Submit a text: lkjh
# Submit a text: mnbv
# Submit a text: CLOSE