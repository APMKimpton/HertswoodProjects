#Guessing Game Homework
#Antony Kimpton

#Imports:
import random
import shelve #<-- Saw this on the docs

#Varibles
def main():
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
               "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    SCORE = 0
    
    generate = True
    guessed = False
    
    #Proc/Func    
    def program(guess,tries,score):
        if guess < computer_number:
            print("Too low, you're guesses are now:",tries," and you guessed the letter: "+guess)
            print("Try again!")
            return False
        elif guess > computer_number:
            print("Too high, your guesses are now:",tries," and you guessed the letter: "+guess)
            print("Try again!")
            return False
        else:
            print("Welldone you have won in",tries, "guesses! With the letter: "+guess)
            #Checks if they beat the last guy:
            if tries < score:
                print("Congrats you beat the last person by", score-tries)
                name = input("Please enter the name you'd like to be know as (case sensitive): ")
                #saves:
                file = shelve.open('score.txt')
                file['score'] = tries
                file['name'] = name
                file.close()
            elif tries == score:
                print("Sadly you only evened with the last person")
                print("They were first so you will not be added to the scoreboard! Sorry")
            else:
                print("You didn't beat the last person - restart the program and try again!")
            return True
    
    #Grab Old Score (If One)
    try: #see's if it exists, if not then it doesnt load
        file = shelve.open('score.txt')
        SCORE = int(file['score'])
        NAME = file['name']
        file.close()
        print("The highest score so far was", NAME, "with only", SCORE, "tries!")
    except:
        print("You are the first player! Either the scoreboard has been deleted or an error appead.")
    
    #Introduction
    print("Hello welcome to Kimpton's Letter Guessing Game, I have generated a random letter!")
    print("Soon I will ask you to guess it")
    print("Press Enter to continue")
    input()
    print("Okay, please enter a letter (Caps lock does not matter! This program only accepts the first letter)")
    
    while guessed != True:
        while generate:
            subscript = random.randint(0,25)
            computer_number = letters[subscript] #I didnt have to pass this in.. (later) hmm
            number_of_guesses = 0
            generate = False
        
        user_guess = input("Letter: ")
        number_of_guesses = number_of_guesses+1
        
        #Validation
        lower_user_guess = user_guess.lower()
        generate = True
        if lower_user_guess.isdigit() == True:
            print("Thats not a letter.. It's a number!")
            print("You have been penaltied a guess. You current guesses are:",number_of_guesses)
                
        else: #Saw this on the doc's, solved the long validation haha (Other was was 4x to 5x this size)
            USER_GUESS = list(lower_user_guess)
            generate = program(USER_GUESS[0], number_of_guesses, SCORE)
            if generate == True:
                print("Press Enter to restart the program")
                input()
                print("Okay, please enter a letter (Caps lock does not matter! This program only accepts the first letter)")
                
if __name__ == "__main__": main()
        

