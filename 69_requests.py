import requests

print(requests.__spec__)

headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get("http://www.pythonhow.com", headers = headers)
print(r.text[:100])


# First, rename the file to another. In this case, 69_requests.py. Run again and the output is:
# ModuleSpec(name='requests', loader=<_frozen_importlib_external.SourceFileLoader object at 0x000001A4B6986490>, origin='C:\\Users\\GayCalaranan.000\\anaconda3\\lib\\site-packages\\requests\\__init__.py', submodule_search_locations=['C:\\Users\\GayCalaranan.000\\anaconda3\\lib\\site-packages\\requests'])
# <!DOCTYPE html>
# <!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en-US"> <![endif]-->
# <!--[if I

# Answer: 
# Rename the file name from requests.py  to something else.

# Explanation:

# In the code, Python is actually referring to the script name, which is requests  And it doesn't find a get attribute for that name. 
# Script names load in the current namespace. They are actually stored in the __name__  variable. 
# You could try to print that variable out, and you would see that it prints your script name. 
# Therefore you should not name your scripts under library names. 