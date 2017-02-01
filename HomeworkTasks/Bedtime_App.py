#Antony Kimpton
#BedTime Calculator
#School Homework

#IMPORTS
import time
import string

#FUNCTIONS AND PROCEDURES

def calcSleep(name, age):
    if age < 7:
        print (name, "should go to bed at 6pm")
        time.sleep(5)
    elif age <11:
        bedtime = age - 1
        print (name, "should go to bed at",str(bedtime))
        time.sleep(5)
    else:
        print (name, "can go to bed at 10pm")
        time.sleep(5)

def getAge(name):
    age = input("How old is "+name+"? ")
    if age.isdigit():
        age = int(age)
        calcSleep(name, age)
    else:
        print ("That is not a number! Try again...")
        getAge(name)

def getName():
    childName = input ("What is your child's name? ")
    if childName.isdigit():
        print ("That wasn't a name was it... try again!")
        getName()
    else:
        getAge(childName)

#ProgramStart:

getName()
