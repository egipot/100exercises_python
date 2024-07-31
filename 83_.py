#83 - Monitor Size Detector

# Question: Write a script that detects and prints out your monitor resolution.

# Expected output: 
# Width: 1920,  Height: 1080

# Hint: Use the screeninfo  Python third party library.

# Based on the documentation : https://pypi.org/project/screeninfo/ 

from screeninfo import get_monitors

for m in get_monitors():
    print(str(m))


#Output:
# Monitor(x=0, y=0, width=1920, height=1200, width_mm=518, height_mm=324, name='\\\\.\\DISPLAY1', is_primary=True)
# Monitor(x=0, y=1200, width=1920, height=1080, width_mm=294, height_mm=165, name='\\\\.\\DISPLAY2', is_primary=False)


#Ardit answer:
# from screeninfo import get_monitors
 
# width=get_monitors()[0].width
# height=get_monitors()[0].height
 
# print("Width: %s,  Height: %s" % (width, height))
# Explanation:

# We're using the get_monitors  method of the screeninfo  library which can be installed with pip install screeninfo . 
# The get_monitors  method produces a list like [monitor(1920x1080+0+0), monitor(1280x1024+-1280+-31)]  listing all the monitors connected to the computer. 
# Applying [0]  to that list gives the first monitor object out of the list. 
# Applying width  to that monitor, the object gives the width of the monitor, and the same goes for the height  property.