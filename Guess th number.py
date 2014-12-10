import random
import simpleguitk
import math

#Initialize global
num_range = 100
chance = 0
secret_number = 0
i  = 0
guess_list = {0:'',1:'\n Lower', 2:'\n Higher', 3:'\n You win', 4:"You ran out of guesses"}
new_game = ''
# helper function to start and restart the game
    
def new_game():
    global new_game
    new_game ='\nSelect the Range you want to play.'
    i = 0
    chance = 0
    
# define event handlers for control panel
def range100():
    global secret_number, chance, new_game
    chance = 7
    new_game = "\nRange is from 0 to 100"
    print ("Number of remaining guesses is", chance)
    secret_number = random.randint(0,100)
    
def range1000():
    global secret_number, chance, new_game
    chance = 10
    secret_number = random.randint(0, 1000)
    new_game = "\nRange is from 0 to 1000"
    print ("Number of remaining guesses is", chance)
    
def input_guess(guess):
    global secret_number, chance, i
    n = int(guess)
    print ('')
    print ("Guess was", guess)
    chance -= 1
    
    
    if n > secret_number and chance >= 0:
        i = 1
        #print ("Lower!")
        #print ("Number of remaining guesses", chance)
    elif n < secret_number and chance >= 0:
        i = 2
        #print ("Higher")
        #print ("Number of remaining gueses", chance)
    elif n == secret_number and chance >= 0:
        i = 3
        #print ("You win!")
        #print ("The secret number was", secret_number)
    else:
        i = 4
        #print ("You ran out of guesses, secret number was:", secret_number)

def draw(canvas):
    global i, guess_list, new_game
    
    canvas.draw_text(new_game, [10, 100], 13, "Yellow")
    if chance>= 1:
        canvas.draw_text(str(guess_list[i]), [50, 150],20, "White")
        canvas.draw_text(str(chance), [50, 200], 20, "White")
    else:
        canvas.draw_text(str(guess_list[i]), [10, 150],14, "Red")
	
    
# create frame
frame = simpleguitk.create_frame("Guess the Number", 300, 300)

# register event handlers for control elements and start frame
frame.set_draw_handler(draw)
frame.add_button("New Game", new_game, 200)
frame.add_button("Range 0-100", range100, 200)
frame.add_button("Range 0-1000", range1000, 200)
frame.add_input("Input your Guess here:", input_guess, 200)


# call new_game 
range100()
