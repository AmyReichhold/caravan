from random import randint
import os
import time


class Board():
    def __init__(self, value, suit):


        # There are three columns of caravans. Keeps track of when a caravan
        # is sold in a column.
        self.tracksSold = 0

class Track():
    def __init__(self):
        self.rows = []
        self.length = 0
        self.value = 0
        self.sold = 0
        self.owner = None   # (Not sure if we need this.)

    def placeCard():
        return
    
    def discard():
        self.rows = []
        self.length = 0
        self.value = 0
        self.sold = 0


class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class Player():
    def __init__(self):
        self.deck = []
        self.deckLen = 0

        self.hand = []

        self.tracksSold = 0


    def setUpDeck(self):
        self.deck = []
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        suits = ["hearts", "diamonds", "spades", "clubs"]
        idx = 0
        for value in values:
            for suit in suits:
                self.deck.append(Card(value, suit))
                # currCard = deck[idx]
                # print(currCard.value, currCard.suit)
                # idx+=1
        #return self.deck


    def drawCard(self):
        cardNum = randint(0, self.deckLen-1)
        self.hand.append(self.deck[cardNum])

        self.deck.pop(cardNum)
        self.deckLen -= 1


    def dealHand(self):
        self.hand = []
        self.deckLen = len(self.deck)
        for i in range(8):
            self.drawCard()
            '''
            #print(f'deckLen = {self.deckLen}')
            cardNum = randint(0, self.deckLen-1)
            #print(f'cardNum = {cardNum}')
    
            currCard = self.deck[cardNum]
            self.hand.append(currCard)
            #print(currCard.value, currCard.suit)
    
            self.deck.pop(cardNum)
            self.deckLen -= 1
            '''


    def discardCard(self, cardNum):
        if self.deckLen == 0:
            print("Can't discard card because deck is empty.")
        else:
            self.hand.pop(cardNum)
            self.drawCard()


    def printHand(self):
        print(f"Player's Hand                   (Deck Length:{self.deckLen})")
        for i in range(len(self.hand)):
            currCard = self.hand[i]
            print(f'{i+1}: {currCard.value} {currCard.suit}')
        print()


def displayBoard(user):
    os.system("clear")
    print("Press 'Q' to quit the game.")
    print()
    print("Opponent's Caravans")
    print("Player's Caravans")
    print("1       2      3")
    print()

    user.printHand()


def setUpPlayer(playerName):
    playerName.deck = setUpDeck()
    playerName.hand = dealHand(playerName.deck)


def main():
    # setUpPlayer(user)
    # setUpPlayer(computer)
    user = Player()
    comp = Player()
    user.setUpDeck()
    user.dealHand()

    '''
    # Initial round to set up caravans.
    initialRound = True
    turn = "user"
    while initialRound == True:
        displayBoard(user)
        print("1. Select Card to start one of your caravans.")
        playerChoice = input()
        # Check if the player wants to quit the game.
        if playerChoice == 'q' or playerChoice == 'Q':
            gameRunning = False
        else: # The player picked a card.
            card = int(playerChoice)
            print("Which caravan would you like to start?")
            if turn == "user":
                pass
    '''


    gameRunning = True
    while gameRunning == True:
        displayBoard(user)
        print("You have 3 choices:")
        print("1. Select Card")
        print("2. Discard Card")
        print("3. Discard Track (but not this one yet lol)")
        playerChoice = input()
        #print(f'playerChoice = {playerChoice}')
        #time.sleep(1)
        # Check if the player wants to quit the game.
        if playerChoice == 'q' or playerChoice == 'Q':
            gameRunning = False
        else: # The player is doing one of the three options.
            playerChoice = int(playerChoice)
            if playerChoice == 1:
                print("Which card would you like to select?")
                card = int(input())
            elif playerChoice == 2:
                print("Which card would you like to discard?")
                cardNum = int(input())
                user.discardCard(cardNum-1)


#user = Player()
#computer = Player()
main()
