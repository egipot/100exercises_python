#Create a script that let the user type in a search term and opens and search on the browser for that term on Google

import webbrowser

query = input("Enter your Google query: ")

#url = "https://www.google.com/?gws_rd=cr,ssl&ei=NCZFWIOJN8yMsgHCyLV4&fg=1#q=%s" % str(query)  --does not work anymore

# https://www.google.com/search?q=tomato+types
url = 'www.google.com/search?q=%s' % str(query)

webbrowser.open_new(url)


#Explanation:

# We're using webbrowser  here which is a standard library that is used to open a web browser.
# First, we're getting the search term stored in variable query via the input  function. 
# You need to first do a manual search on Google and observe how Google will construct the URL. 
# Depending on where you are in the world the URL may be different, but the above URL should work everywhere.
# You will see that the URL contains your search term at the end. 
# Therefore, we concatenate the first part of the URL with the search term we get from input .