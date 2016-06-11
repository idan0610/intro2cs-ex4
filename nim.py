######################################################################
# FILE: nim.py
# WRITER: Idan Refaeli, idan0610, 305681132
# EXERCISE: intro2cs ex4 2014-2015
# DESCRIPTION:
# A simple nim game
#######################################################################
from computer_functions import get_computer_move, HEAPS

heaps = list(HEAPS)

def empty_board(heeps):
    '''
    Check if the board is empty
    
    a function the gets board values and
    returns True if the board is empty
    
    input: list 'heaps' stands for a board
    output: True for empty, False for not empty
    '''
    for i in range(len(heeps)):
        if heeps[i] != 0:
            return False
    return True
    
def print_board(heaps):
    '''
    Builds the board and print it
    
    a function the gets a game board and 
    prints a board on screen
    
    input: list 'heaps' stands for a board
    output: none
    '''
    for i in range(len(heaps)):
        print (str(i+1) + ":")
        if heaps[i] == 0:
            #if the row is empty, prints and empty line
            print()
        else:
            for j in range(heaps[i]):
                #prints * with space, exept the last * without space,
                #according the number of heeps on each row
                if j != heaps[i]-1: 
                    print("*", end=" ")
                else:
                    print("*")
    
            
num_Of_Players = int(input ("Please enter the number of human players \
(1 or 2):"))

computer = False #if the computer is a player, it will become True

if num_Of_Players == 1:
    #computer is playing
    player_One = input("Please enter your name:")
    player_Two = "Computer"
    computer = True
else:
    #2 human beings playing
    player_One = input("Name of first player:")
    player_Two = input("Name of second player:")

current = player_Two #the current player will change with every new run
                     #of the loop, so on the first run, it will be player 1

#For a start, the row number and how many heaps is 0, and that will change
#in every move to the user choices
row = 0 
how_Many = 0

while not empty_board(heaps):
    #on each turn replace the player:
    if current == player_One:
        current = player_Two
    else:
        current = player_One

    print_board(heaps) #prints the current board

    if (current != "Computer" and computer) or not computer:
    #if the player is a human
        print(current + ", it's your turn:")
        while (row <= 0 or row > len(heaps)):
            #asks for a row number until the input is legal         
            row = int(input("Row?"))
            if row > 0 and row <= len(heaps) and heaps[row-1] == 0:
                #becase the rows on heaps start with 0, we check if the chosen
                #row - 1 is empty
                print("That row is empty")
                row = 0 #reset row to start again the while loop
        while (how_Many <= 0 or how_Many > heaps[row-1]):
            #asks for number of heeps to remove, until the input is legal
            how_Many = int(input("How many?"))
    else:
        #get choices of computer from get_computer_move(heaps) function
        pc_Choices = get_computer_move(heaps)
        row = pc_Choices[0] + 1 #the computer choose a row start from 0, so we
                                #need to add 1 to make it a proper row
        how_Many = pc_Choices[1]
        print("Computer takes", how_Many, "from row", row)
    
    #change the board according to player's request, and reset row and how_Many
    heaps[row-1] -= how_Many #the chosen row is actually row - 1 on heaps
    row = 0
    how_Many = 0

    if empty_board(heaps):
        print_board(heaps) #if the game is over, print blank board
        
        #the current player is the winner, we check who he is:
        if current == player_One:
            if computer:
                print("You win")
            else:
                print(player_One, "wins")
        else:
            print(player_Two, "wins")
            
        again = input("Play again? (Y/N)")
        
        if again == "y" or again == "Y":
            #if the players choose to play again, reset the board, row and
            #how_Many, as it was on the first game
            heaps = list(HEAPS)
            row = 0
            how_Many = 0
            
            #if the players want to play again, the winner will be the second
            #player and the loser will be the first, but that will change
            #when the game starts again
            if current == player_One:
                current = player_Two
            else:
                current = player_One
