#Exercise 73
#Multiply by two the values of the text file in the URL  
#Hint: The easiest way to do this is with pandas.

import pandas as pd

data = pd.read_csv('https://pythonhow.com/media/data/sampledata.txt', sep = ',')
#print(data)

new_data = data * 2
#print(new_data(data))
#print(type(new_data))

new_data.to_csv('73_new_multiplied_data.txt', index = None)

