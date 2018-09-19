"""
New topic. Write the same block of code in a function and call that function 10 times
"""
import random

def EvenOdd():
    acc=0
    for i in range(10):
        x = random.randint(0,100)
        if x % 2 == 0:
            print(x, "is an even number")
            acc +=1
        else:
            print(x, "is not an even number")
    print("The number of evens was:", acc)
    
def greeting():
    name=input("Hello. Tell me your name.")
    print(name, "is a weird name.")
    return name
greeting()
def age():
    age=int(input("What is your age?"))
    print(age, "is a bad age")
    return age