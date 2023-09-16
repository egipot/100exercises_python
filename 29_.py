# Question:  Please write a function that calculates liquid volume in a sphere using the following formula. The radius r  is always 10, so consider making it a default parameter.
# You can then test your solution by passing 2 for h and you should get the expected output.

# Hint: Your function should start with something like def volume(h, r = 10): 


#egi solution:
def volume (height, radius = 10):
    pi = 3.141592653589793238462643
    liquid_volume = ((4*pi*(radius**3))/3) - ((pi*(height**2)*(3*radius - height)/3))
    print(liquid_volume)

volume(2)

#4071.5040790523717

#mistake : use **, not ^
#print(10^3) = 9
#print(10**3) = 1000

#use return function - revised
def volume_2 (height2, radius2 = 10):
    pi = 3.141592653589793238462643
    liquid_volume = ((4*pi*(radius2**3))/3) - ((pi*(height2**2)*(3*radius2 - height2)/3))
    return liquid_volume

print(volume_2(2))
#4071.5040790523717