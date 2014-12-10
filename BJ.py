# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
hand_value = 0
test = 0
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
        
class Hand:
    global hand_value
    def __init__(self):
            # create Hand object
        self.hand_cards = []

    def __str__(self):
        a = '' # return a string representation of a hand
        for i in range(len(self.hand_cards)):
            a += ' '+ str(self.hand_cards[i])
        return 'Hand contains'+ a

    def add_card(self, card):
        self.hand_cards.append(card)	# add a card object to a hand

    def get_value(self):
        global hand_value
        i = 0
         
        for i in range(len(self.hand_cards)):
            #print i
            q = str(self.hand_cards.pop())
            w = list(q)
            hand_value += VALUES[w[1]]
        return hand_value	#Value of the Cards
   
    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards
    
    
 
        
# define deck class 
class Deck(Card):
    def __init__(self):
        self.deck = 'Deck Contains '	
        self.cards = []
        for s in SUITS:
            for r in RANKS:
                self.cards.append(Card(s,r))


    def shuffle(self):
        # shuffle the deck 
        return random.shuffle(self.cards)    

    def deal_card(self):
        return self.cards.pop()	# dealing a card object from the deck
    
    def __str__(self):
        a = ""
        for i in range(len(self.cards)):
            a += str(self.cards[i]) + ' '
        return str(self.deck) + str(a)	# representing the deck        
  



#define event handlers for buttons
def deal():
    global outcome, in_play
    i = 0
    
    in_play = True
    # your code goes here
    deck = Deck()
    deck.shuffle()
    dealer_hand = Hand()
    player_hand = Hand()
    dealer_hand.add_card(deck.deal_card())
    
    player_hand.add_card(deck.deal_card())
    
    print 'player',player_hand
    print 'Value:',player_hand.get_value()
    print 'dealer',dealer_hand
    print 'Value:',dealer_hand.get_value()
    in_play = True
    
    

def hit():
    global in_play
     
    deck = Deck()
    deck.shuffle()    
    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    print 'player', player_hand
    v = 0
    v = int(player_hand.get_value())
    while in_play:
        if v <= 21:
            player_hand.add_card(deck.deal_card())
            v += player_hand.get_value()
            #
            print 'Player hand value:',v
        else:
            in_play = False
            print 'Busted!'
 
    
       
def stand():
    global test, in_play
    #test = Hand()	
    deck = Deck()
    deck.shuffle()
    
    while in_play:
        if test <=17:
            dealer_hand = Hand()
            #player_hand = Hand()
            dealer_hand.add_card(deck.deal_card())
            print dealer_hand
            test += int(dealer_hand.get_value())
            print test
        else:
            in_play = False
            print 'Busted!'
    
    score = test

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card('S','A')
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
