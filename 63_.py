#Exercise 63 - Progressive Time Printer with Threshold

#Question: Create a program that, once executed the programs prints Hello  instantly first, 
#then it prints it after 1 second, then after 2, 3, and then the program prints out the message "End of the Loop" and stops.

#Expected output: 
#Hello
#Hello
#Hello
#Hello
#End of Loop

#Solution 1 (without seeing the Hint)
import time

i = 0

while i <=3 :
    time.sleep(i)
    print('Hello')
    i += 1

print('End of Loop')


#Solution 2 (after seeing the Hint)
#Hint: Include an if  statement inside the loop and a break  statement inside the conditional.
i = 0
threshold = 4
while i <= threshold:
    print('Hello')
    time.sleep(i)
    i+=1
    if i == threshold:
        break
print('End of Loop')


#Ardit's answer:
j = 0
while True:
    print("Hello")
    j = j + 1
    if j > 3:
        print("End of Loop")
        break
    time.sleep(j)
    