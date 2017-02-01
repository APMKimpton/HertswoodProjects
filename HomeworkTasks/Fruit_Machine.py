import random
import time

#Fruits
fruits = ['banana', 'lemon', 'cherry', 'watermelon', 'tomato', '7']

#Welcome
print("Welcome to the LEGIT AND TOTALLY NOT FIXED Kimpton Fruit Machine")
print("This fruit machine costs £10 a go!")

#Money
def money():
    money_in = float(input("Please enter some money: "))
    if money_in <10:
        print ("Your money has been returned, please put £10 or more!")
        return 0
    else:
        turns = int(abs(money_in/10))
        value = str(turns*10)
        print("Any money over " + value + " has been returned to you below")
        print("You have " + str(turns) + " turns!")
        return turns

def start():    
    turns = money()
    while turns < 1:
        turns = money()
        
    return turns

turns = start()

figure = (len(fruits)-1)

while turns+1 > 0:
    turns-1
    col1 = random.randint(0,figure)
    col2 = random.randint(0,figure)
    col3 = random.randint(0,figure)
    if turns > 0:
        print("You have £" +str(turns*10)+" in your account!")
        print("Press the cash out key to redeem your money or...")
        print("Press any key to roll")
        input()
        print(fruits[col1]+"  "+fruits[col2]+"  "+fruits[col3])
        print(" ")
        turns = turns - 1
        if fruits[col1] == fruits[col2] and fruits[col2] == fruits[col3]:
            print("You have hit the jack pot! £50 has been added to your account!")
            turns = turns + 5
        elif fruits[col1] == fruits[col2] or fruits[col2] == fruits[col3]:
            print("You matched two! £20 has been added to you account!")
            turns = turns + 2
        else:
            print("You did not match anything!")

    else:
        print (" ")
        print("You have ran out of intial money.")
        print("Program is rebooting...")
        time.sleep(3)
        turns = turns+start()
        
  
