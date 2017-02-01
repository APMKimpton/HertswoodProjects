'''
Created on 18 Oct 2014

@author: Antony Kimpton
'''
def main():
    #Here is the basic board  
    rows = [[" "," "," "],[" "," "," "],[" "," "," "]]
    
    two_player(rows) #Will expand for AI.... Eventually

def two_player(rows):
    won = False
    print("This is two player O's and X's")
    print("Player 1 is X's and Player 2 is O's")
    print("The current board looks like:")
    prt_multirow(rows)
    
    while won != True:
        print("Player 1")
        game(rows, 1)
        player1 = checker(rows)
        won = player1
        winner = 1
        if full(rows) == True: won = True
        if won != True: #Else player 2 got an extra turn
            print("Player 2")
            game(rows, 2)
            player2 = checker(rows)
            won = player2
            winner = 2
            if full(rows) == True: won = True
    if checker(rows) == True or full(rows) == checker(rows):
        print("Player " + str(winner) + " has won!")
    else:        
        print("Noone won!")
        
    print("Press Enter to play again or Alt+F4 to exit:")
    input('')
    main()       
    
def game(r, player=1):
    row = input("Please enter 1, 2 or 3 for a row: ")
    row = vali(row)
    if row == 5:
        game(r, player)
        return None
    print("You have selected row: ",row+1)             
    col = input("Please enter 1, 2 or 3 for a column: ")
    col = vali(col)
    if col == 5:
        game(r, player)
        return None
    print("You have selected column: ",col+1)
        
    if r[row][col] == " ":
        if player == 1:
            r[row][col] = "X"
        elif player == 2:
            r[row][col] = "O"
        print("The current board is: ")
        prt_multirow(r)
    else:
        print("Sorry that spot is taken already: ")
        prt_multirow(r)
        print("See..? Try again")
        game(r, player)
    
def checker(r): #Has someone won?
    for i in range(0,3):
        #Across
        if r[i][0] == r[i][1] and r[i][0] == r[i][2] and r[i][0] != " ":
            return True  
        #Down
        elif r[0][i] == r[1][i] and r[0][i] == r[2][i] and r[0][i] != " ":
            return True
    #L to R Diag 
    if r[0][0] == r[1][1] and r[0][0] == r[2][2] and r[0][0] != " ":
        return True
    #R to L Diag
    elif r[0][2] == r[1][1] and r[0][2] == r[2][0] and r[0][2] != " ":
        return True
    else:
        return False
    
def full(r):
    for i in range(0,3):
        for j in range(0,3):
            if r[i][j] == " ":
                return False
    return True
    

#Prints current board
def prt_multirow(r):
    for i in range(0,3):
        print(r[i][0]+"|"+r[i][1]+"|"+r[i][2])
        
def vali(v):    
    try:
        var = int(v[0])
        if var < 4 and var > 0:
            return var-1
        else:
            print("You did not enter a value between 1-3, please try again")
            return 5
    except:
        print("You did not enter a number, please try again")
        return 5
    
    
    
#Conditional - Allows me to boot the main function, start of the program   
if __name__ == "__main__": main()
