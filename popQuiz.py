"""
Print a number between -5 and 5
"""

import random

print ("Your random number between -5 and 5 is: ",random.randint(-5,5))

"""
Print a random integer between 0 and 100 50 times
"""

print("We will now print a number between 0-100 500 times: ")

for x in range(500):
    print(random.randint(0,100))
    
"""
Print a random number and determine if it is even or odd
"""
print("We will now determine if a random number is even or odd")
x = random.randint(0,100)
if x % 2 ==0:
    print(x ,"is an even number")
else:
    print(x ,"is not an even number")
"""
Print 10 random numbers and determine if they are even or odd
"""
print("We will now print 10 random numbers and determine if they are even or odd.")
for i in range(10):
    x = random.randint(0,100)
    if x % 2 == 0:
        print(x, "is an even number")
    else:
        print(x, "is not an even number")
"""
Modify the code in part 4 that will add up the number of even numbers and print that result. Use accumulator
"""
acc=0
for i in range(10):
    x = random.randint(0,100)
    if x % 2 == 0:
        print(x, "is an even number")
        acc +=1
    else:
        print(x, "is not an even number")
print("The number of evens was:", acc)

