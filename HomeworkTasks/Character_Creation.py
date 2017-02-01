#Imports
import random
import sys

#SKILLS
STR = 10
INT = 10
DEX = 10
VIT = 10
LUCK = 0

#Functions and Procedures
def program_begin():  #first function - asks user if they are male or female  
    gender = str(input ("What gender are you, M/F? "))
    GENDER = mf_check(gender)
    if GENDER == 0:
        return 0
    elif GENDER == 1:
        return str("Male")
    else:
        return str("Female")
    
def skill_calc(x):      #Finds the random numbers for skills
    dice_one = random.randint(1,4)
    dice_two = random.randint(1,12)
    value = int(abs(dice_two/dice_one))
    return x + value
    
def mf_check(y):        #Conditions to check Male/Female
    if y.lower() == str("m"):
        return 1
    elif y.lower() == str("f"):
        return 2
    elif y.lower() == str("male"):
        return 1
    elif y.lower() == str("female"):
        return 2
    else:
        print (" ")
        print ("You did not specify clearly enough what gender you are.")
        print ("Please write either M, F, MALE or FEMALE.")
        print ("Try again...")
        print (" ")
        return 0
    
def program(x):
    name = input ("...and what is your name? ")

    #Skills
    Str = str(skill_calc(STR))
    Int = str(skill_calc(INT))
    Dex = str(skill_calc(DEX))
    Vit = str(skill_calc(VIT))
    Luck = str(skill_calc(LUCK))

    print (" ")
    print ("Your character has been generated with some random stats:")
    for i in range(2): #first prints the values out
        if i == 0:
            y = print
        else:          #then writes them to a file
            save = open(name+".txt", 'w')
            y = save.write
        y(" ")
        y("*      NAME: " + name)
        y("*    GENDER: " + x)
        y("*  STRENGTH: " + Str)
        y("* INTELLECT: " + Int)
        y("* DEXTERITY: " + Dex)
        y("*  VITALITY: " + Vit)
        y("*      LUCK: " + Luck)
    save.close()

def checker(x): #makes a loop for the program if they cant spell m/f
    if x == 0:
        x = program_begin()
        checker(x)        
    else:
        program(x)
    
#Program Starts Here!
print ("Hello there, welcome to World of Skill")
print ("We're going to create you a character!")
GENDER = program_begin()
checker(GENDER)



    
 
