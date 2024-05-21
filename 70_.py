# Exercise 70 - File from URL

# Question: Print out the text of this file https://pythonhow.com/media/data/universe.txt

# Don't manually download the file. Let Python do all the work.

# Expected output: 

# Distant regions of space are assumed to exist and to be part of reality as much as we are, even though we can never
# interact with them. The spatial region that we can affect and be affected by is the observable universe. The observa
# ble universe depends on the location of the observer. By traveling, an observer can come into contact with a greater
# region of spacetime than an observer who remains still. Nevertheless, even the most rapid traveler will not be able
# to interact with all of space. Typically, the observable universe is taken to mean the portion of the Universe that
# is observable from our vantage point in the Milky Way.

import requests

text = requests.get('https://pythonhow.com/media/data/universe.txt')

print(text) #<Response [200]>
print(text.content)
#b'Distant regions of space are assumed to exist and to be part of reality as much as we are, even though we can never interact with them. The spatial region that we can affect and be affected by is the observable universe. The observable universe depends on the location of the observer. By traveling, an observer can come into contact with a greater region of spacetime than an observer who remains still. Nevertheless, even the most rapid traveler will not be able to interact with all of space. Typically, the observable universe is taken to mean the portion of the Universe that is observable from our vantage point in the Milky Way.'
print(text.status_code) #200
print(text.text)
#Distant regions of space are assumed to exist and to be part of reality as much as we are, even though we can never interact with them. The spatial region that we can affect and be affected by is the observable universe. The observable universe depends on the location of the observer. By traveling, an observer can come into contact with a greater region of spacetime than an observer who remains still. Nevertheless, even the most rapid traveler will not be able to interact with all of space. Typically, the observable universe is taken to mean the portion of the Universe that is observable from our vantage point in the Milky Way.


#ardit answer:
# import requests
# response = requests.get("http://www.pythonhow.com/data/universe.txt", headers = {'user-agent': 'customUserAgent'})
# text = response.text
# print(text)
# Explanation:

# We're using the get method of the requests  library here, which produces a response  object in line 2. Then, in line 3, we apply the text property to that response object to get the loaded web page's text.