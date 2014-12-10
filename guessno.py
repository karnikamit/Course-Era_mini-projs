import random
import simpleguitk
import math
#Initializing globals

chance = 7
chance1 = 10

secret_number = 0
# helper function to start and restart the game
    
def new_game():
    
    global chance, chance1
    chance = 7
    chance1 = 10
    
     

def range100():
    print ('')
    global secret_number, chance
    print ("New game. Range is from 0 to 100")
    print ("Number of remaining guesses is", chance)
    secret_number = random.randint(0,100)

def range1000():
    print ('')
    global secret_number, chance1
    secret_number = random.randint(0, 1000)
    print ("New game. Range is from 0 to 1000")
    print ("Number of remaining guesses is", chance1)    

# Main Code
def input_guess(guess):
    global secret_number, chance
    n = int(guess)
    print ('')
    print ("Guess was", guess)
    chance = chance - 1
    if n == secret_number and chance >= 0:
        print ("Number of remaining gueses is", chance)
        print ("You win!")
        new_game()
        range100()
    
    elif chance == 0:
        print ("Number of remaining gueses is", chance)
        print ("You ran out of guesses. Secret number was", secret_number)
        new_game()
        range100()
        
    elif n < secret_number and chance >= 0:
        print ("Number of remaining gueses is", chance)
        print ("Higher!")
        
    elif n > secret_number and chance >= 0:
        print ("Number of remaining gueses is", chance)
        print ("Lower!")

        
def input_guess1(guess1):
    
    global secret_number, chance1
    n = int(guess1)
    print ('')
    print ("Guess was", guess1)
    chance1 = chance1 - 1
    if chance1 == 0:
        print ("Number of remaining gueses is", chance1)
        print ("You ran out of guesses. Secret number was", secret_number)
        new_game()
        range1000()
    
    elif n < secret_number and chance1 >= 0:
        print ("Number of remaining gueses is", chance1)
        print ("Higher!")
    elif n == secret_number and chance1 >= 0:
        print ("Number of remaining gueses is", chance1)
        print ("Correct!")
        new_game()
        range1000()
        #print "The secret number was", secret_number
    elif n > secret_number and chance1 >= 0:
        print ("Number of remaining gueses is", chance1)
        print ("Lower!")
    
# create frame
frame = simpleguitk.create_frame("Guess the Number", 300, 300)

# register event handlers for control elements and start frame
frame.add_button("Range 0-100", range100, 200)
frame.add_button("Range 0-1000", range1000, 200)
frame.add_input("Guess0-100", input_guess, 200)
frame.add_input("Guess0-1000", input_guess1, 200)
frame.add_button("Restart", new_game, 80 )
frame.set_canvas_background('Red')
# call new_game 
#new_game()
#range100()
