# Exercise 61 - Timed Printer
# Question: Create a program that prints out Hello  every two seconds.
#Expected output:
#Hello
#Hello
#Hello
#Hello
#Hello
#Hello
#...

#Egi answer:
import time

while True:
    print('Hello')
    time.sleep(2)

#Hint: Make the program sleep  for two seconds using the time  module.