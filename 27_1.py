#Create a function that calculates acceleration.

#egi
#not following directions - you should have used a function!
velocity2 = int(input("velocity2: "))
velocity1 = int(input("velocity1: "))
starttime = int(input("starttime: "))
endtime = int(input("endtime: "))
acceleration = ((velocity2 - velocity1))/(starttime-endtime)
print (acceleration)

#Answer (Python 3): 

def acceleration(v1, v2, t1, t2):
    a = (v2 - v1) / (t2 - t1)
    return a
 
print(acceleration(0,10,0,20))


#Explanation (Python 3): 
#The first three lines are where we create the function. A function definition is like a like a blueprint. Then in the last line, we're printing out the function output. The output is whatever is returned by the return  statement.

#Answer (Python 2): 

def acceleration(v1, v2, t1, t2):
    a = float(v2 - v1) / float(t2 - t1)
    return a
 
print(acceleration(0,10,0,20))

#Explanation (Python 2): 
#If you were creating this in Python 2, the solution would need to have two float  functions converting the two differences to float numbers because if the differences are integers, Python will also output an integer (e.g., 3 / 2 outputs 0). 
#In Python 3, you don't have to convert to floats.