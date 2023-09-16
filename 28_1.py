#Question:  Why is there an error in the code, and how would you fix it?
#Hint: This function needs to return something to be complete.
def foo(a, b):
    print(a + b)
    return a+b #egi
 
x = foo(2, 3) * 10
print(x)

#Ardit answer: 

#Line 4 throws a TypeError because Python cannot multiply a None type object with an integer. The function output is what produces a None object because the function definition is not returning anything. Fix it by using return  instead of print :

def foo(a, b):
    return a + b
 
x = foo(2, 3) * 10
print(x)

