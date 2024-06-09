from random import randint
import os
import time


class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class Player():
    def __init__(self):
        self.deck = []
        self.hand = []
        self.c1 = []
        self.c2 = []
        self.c3 = []


def setUpDeck():
    deck = []
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    suits = ["hearts", "diamonds", "spades", "clubs"]
    idx = 0
    for value in values:
        for suit in suits:
            deck.append(Card(value, suit))
            # currCard = deck[idx]
            # print(currCard.value, currCard.suit)
            # idx+=1
    return deck

def drawCard(deck):
    deckLen = len(deck)
    cardNum = randint(0, deckLen-1)
    


def dealHand(deck):
    hand = []
    deckLen = len(deck)
    for i in range(8):
        #print(f'deckLen = {deckLen}')
        cardNum = randint(0,deckLen-1)
        #print(f'cardNum = {cardNum}')

        currCard = deck[cardNum]
        hand.append(currCard)
        #print(currCard.value, currCard.suit)

        deck.pop(cardNum)
        deckLen -= 1

    return hand


def printHand(player, hand):
    print(f"{player}'s hand")
    for i in range(len(hand)):
        currCard = hand[i]
        print(f'{i+1}: {currCard.value} {currCard.suit}')


def displayBoard():
    os.system("clear")
    print("Press 'Q' to quit the game.")
    print()
    print("Opponents Caravans")
    print("Playerss Caravans")
    print("C1       C2      C3")
    print(f'{player.c1}       {player.c2}       {player.c3}')
    print()

    printHand("Player", player.hand)

def setUpPlayer(playerName):
    playerName.deck = setUpDeck()
    playerName.hand = dealHand(playerName.deck)


def main():
    setUpPlayer(player)
    setUpPlayer(opponent)

    gameRunning = True
    while gameRunning == True:
        displayBoard()
        print("You have 3 choices:")
        print("1. Select Card")
        print("2. Discard Card")
        print("3. Discard Track (but not this one yet lol)")
        playerChoice = input()
        print(f'playerChoice = {playerChoice}')
        time.sleep(2)
        # Check if the player wants to quit the game.
        if playerChoice == 'q':
            gameRunning = False
        else: # The player is doing one of the three options.
            playerChoice = int(playerChoice)
            if playerChoice == 1:
               cardNumber  = int(input())
            elif playerChoice == 2:
               cardNumber  = int(input())


player = Player()
opponent = Player()
main()
