#C:/Users/Antony/Desktop/Python/School Python/Good Files/Draughts.py
#19 Oct 2014
#
#Antony
def main():#loop to here to restart to program
    board =[["X"," ","X"," ","X"," ","X"," "],
            [" ","X"," ","X"," ","X"," ","X"],
            ["X"," ","X"," ","X"," ","X"," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" ","O"," ","O"," ","O"," ","O"],
            ["O"," ","O"," ","O"," ","O"," "],
            [" ","O"," ","O"," ","O"," ","O"],]
    
    tiles =[["B","W","B","W","B","W","B","W"],
            ["W","B","W","B","W","B","W","B"],
            ["B","W","B","W","B","W","B","W"],
            ["W","B","W","B","W","B","W","B"],
            ["B","W","B","W","B","W","B","W"],
            ["W","B","W","B","W","B","W","B"],
            ["B","W","B","W","B","W","B","W"],
            ["W","B","W","B","W","B","W","B"],]
    two_player(board,tiles) #IDK when i'll get round to making an AI
    
def two_player(b,t):#When bothered: Will make an AI to replace this
    print("Hello and welcome to Kimpton's Draughts!")
    print("This is a two player game - Player 1 you are O's")
    print("Player 2 you are X's (you go second)")
    
    won = False
    while won != True:
        prt_board(b)
        print("Player 1:")        
        player = 1
        game(player,b,t)
        won = winner(player, b)
        if won != True: #Else p2 gets an extra turn if p1 wins
            prt_board(b)
            print("Player 2:")
            player = 2
            game(player,b,t)
            won = winner(player, b)
    print("Player "+str(player)+" has won!")
    input("Press enter to restart or ALT+F4 to close the program")
    main()
            
def game(player,board,tiles):#Can be used by single player
    colour = "B"
    if player == 1:
        target = ("O","K")
    else:
        target = ("X","Q")
    running = True
    while running:
        vali = False
        while vali != True:
            r,  c, vali = selection(1)
            if board[r][c] != target[0] and board[r][c] != target[1]:
                vali = False
                prt_board(board)
                print("Player "+str(player)+":")
                print("That's not one of your counters, try again.")
                continue
            if board[r][c] == target[0]: type = target[0]
            elif board[r][c] == target[1]: type = target[1]
            
        dest = False
        while dest != True:
            r2, c2, dest = selection(2)
            jump = 0
            move, jump = valid_move(r,c,r2,c2,type,board)        
            if move == True:
                board[r2][c2] = type
                type = extra_rules(type, board)
                board[r2][c2] = type
                board[r][c] = " "
                if jump > 0:
                    if jump == 1:
                        board[r+1][c-1] = " "
                    if jump == 2:
                        board[r+1][c+1] = " "
                    if jump == 3:
                        board[r-1][c-1] = " "
                    if jump == 4:
                        board[r-1][c+1] = " "
                running = False
            else:
                prt_board(board)
                print("Player "+str(player)+":")
                print("That is not an area you can go to! Try again")
                continue
        
def valid_move(row1,col1,row2,col2,type,b): #handles validation of moves
    if type == "X" and type != "Q":
        if row1+1 == row2:#Normal
            if col1-1 == col2 or col1+1 == col2 or col1 == col2:
                if b[row2][col2] == " ":
                    return True, 0
                else: return False, 0
            else: return False, 0
                
        elif row1+2 == row2:#Jumping
            if col1-2 == col2:#Left
                if b[row1+1][col1-1] == "O" or b[row1+1][col1-1] == "K":
                    return True, 1
                else: return False, 0
            elif col1+2 == col2:#Right
                if b[row1+1][col1+1] == "O" or b[row1+1][col1+1] == "K":
                    return True, 2
                else: return False, 0
            else: return False, 0
        else: return False, 0
                                              
    elif type == "O" and type != "K":
        if row1-1 == row2:#Normal
            if col1-1 == col2 or col1+1 == col2 or col1 == col2:
                if b[row2][col2] == " ":
                    return True, 0
                else: return False, 0
            else: return False, 0
            
        elif row1-2 == row2:#Jumping
            if col1-2 == col2:#Left
                if b[row1-1][col1-1] == "X" or b[row1-1][col1-1] == "Q":
                    return True, 3
                else: return False, 0
            elif col1+2 == col2:#Right
                if b[row1-1][col1+1] == "X" or b[row1-1][col1+1] == "Q":
                    return True, 4
                else: return False, 0
            else: return False, 0
        else: return False, 0
               
    elif type == "K" or type == "Q":#Normal
        if row1-1 == row2 or row1+1 == row2:
            if col1-1 == col2 or col1+1 == col2 or col1 == col2:
                if b[row2][col2] == " ":
                    return True, 0
                else: return False, 0
            else: return False, 0
        elif type == "K":
            if row1-2 == row2 or row1+2 == row2:
                if b[row1-1][col1-1] == "X" or b[row1-1][col1-1] == "Q":
                    return True, 3
                elif b[row1+1][col1-1] == "X" or b[row1+1][col1-1] == "Q":
                    return True, 1
                elif b[row1+1][col1+1] == "X" or b[row1+1][col1+1] == "Q":
                    return True, 2
                elif b[row1-1][col1+1] == "X" or b[row1-1][col1+1] == "Q":
                    return True, 4 
                else: return False, 0
            else: return False, 0
            
        elif type == "Q":
            if row1-2 == row2 or row1+2 == row2:
                if b[row1-1][col1-1] == "O" or b[row1-1][col1-1] == "K":
                    return True, 3
                elif b[row1+1][col1-1] == "O" or b[row1+1][col1-1] == "K":
                    return True, 1
                elif b[row1+1][col1+1] == "O" or b[row1+1][col1+1] == "K":
                    return True, 2
                elif b[row1-1][col1+1] == "O" or b[row1-1][col1+1] == "K":
                    return True, 4 
                else: return False, 0
            else: return False, 0    
            
        else: return False, 0
    else: return False, 0
        
def extra_rules(type,b): # Handles upgrades to the types
    if type == "O":
         for i in range(0,8):
             if b[0][i] == type:
                 type = "K"
                 return type
             else: return type
    elif type == "X":
         for i in range(0,8):
             if b[7][i] == type:
                 type = "Q"
                 return type
             else: return type
    else: return type      
          
def selection(id=0): #Defaults 'to move to'
    if id == 1:
        i = 'for the counter you wish to move is '
    else:
        i = "you would like to place your counter "
        
    row = input("Please enter which row {}(1 - 8): ".format (i)) #Means I can use for multi-purpose
    row = vali(row)
    if row == 9:
        return 0, 0, False
    
    col = input("Please enter which column {}(1 - 8): ".format(i))
    col = vali(col)
    if col == 9:
        return 0, 0, False
    else:
        return row, col, True
    
def prt_board(b):#Prints the current board in local terms
    print("The current board is: ")
    print("     1   2   3   4   5   6   7   8  ")
    print("    - - - - - - - - - - - - - - - -")
    for j in range(0,8):
        print(" "+str(j+1)+" ", end='| ')
        for i in range(0,8):
            print(b[j][i], end=' | ')
        print(end='\n')
        print("    - - - - - - - - - - - - - - - -")
        
def winner(player, b): #Scans the board to see if opposite user has lost
    if player == 1:
        x = ("X","Q")
    else:
        x = ("O","K")
    print(x[0],x[1])
    for j in range(0,8):
        for i in range(0,8):
            if x[0] == b[j][i] or x[1] == b[j][i]:
                return False
                continue
    return True

def vali(v): #Solves for anything they put in that I don't want!
    try:
        var = int(v[0])
        if var < 9 and var > 0:
            return var-1
        else:
            print("You did not enter a value between 1-8, please try again")
            return 9
    except:
        print("You did not enter a number, please try again")
        return 9  

if __name__ == '__main__': main()#Remember.. this is conventional!