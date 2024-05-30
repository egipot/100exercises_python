#concatenate two text files and save into one text file

#egi answer:
import pandas as pd

data1 = pd.read_csv('https://pythonhow.com/media/data/sampledata.txt')
#print(data1)
data2 = pd.read_csv('https://pythonhow.com/media/data/sampledata_x_2.txt')
#print(data2)

data_all = pd.concat([data1, data2])
#print(data_all)
data_all.to_csv('74_data_all.txt', index = None)


#ardit solution1:
# data1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
# data2 = pandas.read_csv("sampledata_x_2.txt")
# data12 = pandas.concat([data1, data2])
# data12.to_csv("sampledata12.txt", index=None)

# Explanation 1:
# Again we are using pandas to load the data into Python. 
# Then in line 5, we use the concat  method. 
# The method expects as input a list of dataframe objects to be concatenated. 
# Lastly, in line 6, we export the data to a new text file.



#ardit solution2:
# import io
# import pandas
# import requests
 
# r = requests.get("http://www.pythonhow.com/data/sampledata.txt")
# c = r.content
# data1 = pandas.read_csv(io.StringIO(c.decode('utf-8')))
# data2 = pandas.read_csv("sampledata_x_2.txt")
# data12 = pandas.concat([data1, data2])
# data12.to_csv("sampledata12.txt", index=None)

# Explanation 2:
# In answer 1, we passed the file URL directly into read_csv. 
# The read_csv  method uses the urllib  library internally to download the file. 
# In case of errors with urllib you can use the more powerful library requests library as we did above.