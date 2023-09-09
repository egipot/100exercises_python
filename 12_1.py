#Question: 
#Complete the script so that it produces the expected output. Please use my_range  as input data.

#egi solution:
my_range = range(1, 21)

print(my_range) #range(1, 21)
print(list(my_range)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

my_range2 = range(0,210)
print(list(my_range2)[10::10])   #[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

#ardit solution
print([10* x for x in my_range]) #[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
#for loop inside list comprehension []