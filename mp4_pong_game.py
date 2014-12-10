# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH/2, HEIGHT/2]

vel = [-2, -3]
time = 1
pos1 = 0
pos2 = 0
paddle1_pos = [[0,pos1],[0,pos1 + PAD_HEIGHT]]
paddle2_pos = [[WIDTH,pos2],[WIDTH, pos2 + PAD_HEIGHT]] 
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, vel # these are vectors stored as lists
    
    if direction == 'RIGHT' or direction == 'LEFT':
        ball_pos = [300, 200]
    
    #elif direction == 'LEFT':
        #ball_pos == [300, 200]
       
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball('RIGHT')

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, time, vel
    global pos1, pos2
    
    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] = ball_pos[0] + time * vel[0]
    ball_pos[1] = ball_pos[1] + time * vel[1]
    
    #Collision and reflection off Left paddle
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH and ball_pos[1] in range (paddle1_pos[0][1], paddle1_pos[1][1]):
        vel[0] = -vel[0]
    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH and not ball_pos[1] in range (paddle1_pos[0][1], paddle1_pos[1][1]) :
        score2 += 1
        direction = 'LEFT'
        spawn_ball('LEFT')
        
    #Collision and reflection off top wall
    if ball_pos[1] <= BALL_RADIUS:
        vel[1] = -vel[1]
        
    # collision and reflection off bottom wall
    if ball_pos[1] >= HEIGHT - 20:
        vel[1] = -vel[1]
    
    #Collision and reflection off right paddle    
    if ball_pos[0] >= ((WIDTH-1) - PAD_WIDTH)-20 and ball_pos[1] in range (paddle2_pos[0][1], paddle2_pos[1][1]):
        vel[0] = -vel[0]        
    
    if ball_pos[0] >= ((WIDTH-1) - PAD_WIDTH)-20 and not ball_pos[1] in range (paddle2_pos[0][1], paddle2_pos[1][1]):
        score1 += 1
        direction = 'RIGHT'
        spawn_ball('RIGHT')
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos = [[0, pos1],[0,pos1 + PAD_HEIGHT]]
    if paddle1_pos[0][1] < 0:
        pos1 = 0
    
    if paddle1_pos[1][1] >= (HEIGHT - 1):
        pos1 = HEIGHT - PAD_HEIGHT
        
    paddle2_pos = [WIDTH,pos2],[WIDTH, pos2 + PAD_HEIGHT]
    if paddle2_pos[0][1] < 0:
        pos2 = 0
        
    if paddle2_pos[1][1] > (HEIGHT - 1):
        pos2 = HEIGHT - PAD_HEIGHT
    
    
    # draw paddles
    canvas.draw_line([0,pos1],[0,pos1 + PAD_HEIGHT], PAD_WIDTH * 2, 'White')
    canvas.draw_line([WIDTH,pos2],[WIDTH, pos2 + PAD_HEIGHT], PAD_WIDTH * 2, 'White')
    
    # draw scores
    canvas.draw_text(str(score1), [250, 100], 50, "White")
    canvas.draw_text(str(score2), [325, 100], 50, "White")
    
    
def tick():
    global time
    time += 5
    
def keydown(key):
    global paddle1_pos, paddle2_vel, vel, pos1, pos2
    if key == simplegui.KEY_MAP['w']:
        pos1 -= 50
    
    elif key == simplegui.KEY_MAP['s']:
        pos1 += 50
        
    elif key == simplegui.KEY_MAP['up']:
        pos2 -= 50
           
    elif key == simplegui.KEY_MAP['down']:
        pos2 += 50
     
            
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
#frame.set_draw_handler(spawn_ball)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(1000, tick)
frame.add_button('New Game', new_game, 200)

# start frame
#new_game()
frame.start()
#timer.start()
