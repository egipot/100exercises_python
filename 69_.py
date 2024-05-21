# Exercise 69 - Requests

# Question: Please create an empty file (manually as you normally create Python files) and name it requests.py . Make sure the file has that name exactly.

# Then paste the following code into the file:

# import requests
 
# headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
# r = requests.get("http://www.pythonhow.com", headers = headers)
# print(r.text[:100])
# Executing the script will throw an error. Please fix something to make the program print out the expected output. You should not modify the code itself, but something else.

# Expected output: 

# <!DOCTYPE html>
# <!--[if IE 7]>
# <html class="ie ie7" lang="en-US" prefix="og: http://ogp.me/ns#">

#Hint 1: The code generates an error that suggests the requests module does not have a get  method. 
#        The requests library does actually have a get  method.
#Hint 2: Import statements first look for a local file in the current directory (e.g., requests.py). 
#        If there is such a file, it imports that file and not the actual module. 


