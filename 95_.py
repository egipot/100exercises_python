# Exercise 95: Solution

# Exercise for reference: 

# Create a program that asks the user to input values separated by commas 
# and stores those values in a text file, each value in a separate line.

# Hint: Think of splitting the user string.

user_input = input ("Enter values: ")
user_input_csv = [i.strip() for i in user_input.split(',')]
print(user_input_csv)
with open ('95_user_input_.txt', 'a+') as f:
    for i in user_input_csv:
        f.write(i + '\n')


#Self - test: In case the values do not need to be saved in text file and only printed afterwards:
# u_list = '\n'.join(user_input_csv)
# print(u_list)

######################
# Ardit answer: 

# line = input("Enter values: ")
# line_list = line.split(",")
# with open("user_data_commas.txt", "a+") as file:
#     for i in line_list:
#         file.write(i + "\n")
# Explanation:

# In line 1, we ask the user to input the values, and in line 2, we create a list containing the user submitted values. Then, in line 3, we open a file in a+  mode (read and append). If there's no file with such a name, it will be created. 
# Then in lines 4 and 5, we iterate through the list and write those lines in the opened file.