'''
This module contains the main classes for blackjack.py
'''

import random


suits = ('Diamonds', 'Clubs', 'Hearts', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    '''Defines each of the 52 cards in the deck'''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)


class Deck:

    def __init__(self):
        '''Generates the Deck of 52 cards'''
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck = ''
        for card in self.deck:
            deck += '\n' + card.__str__()
        return deck

    def shuffle(self):
        '''Shuffle deck'''
        random.shuffle(self.deck)

    def deal_card(self):
        '''Pop card off of deck to deal'''
        return self.deck.pop(0)


class Hand:
    '''Generate player's hands'''

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def draw(self, card):
        '''Drawing card from Deck() and adding value to total'''
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def aces(self):
        '''Compensate for aces if cards are over 21'''
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def split(self):
        '''Split hand if cards are same value'''
        pass


class Chips:
    '''
    Defines the player's chip bank
    args = amoutn of chips
    '''

    def __init__(self, value):
        self.value = value
        self.bet = 0

    def lose_bet(self):
        self.value -= self.bet

    def win_bet(self):
        self.value += self.win_bet


def ask_chips():
    '''Asks player how many chips they want to start with'''
    while True:
        try:
            bank = int(input("How many chips do you want to buy? - "))
        except ValueError:
            print("Sorry, I didn't understand you, please try again")
            continue
        else:
            if bank < 1:
                print(
                    "You haven't bought enough chips to play, you need to purchase more.\n")
                continue
            else:
                break

    print(f"Thank you!\nYou have bought {bank} chips!")
    return bank


def ask_bet(chips):
    '''Asks player for a bet, cannot be more than their current chip count'''
    while True:
        try:
            chips.bet = int(input("How many chips do you want to bet? - "))
        except ValueError:
            print("Sorry, I didn't understand you, please try again")
            continue
        except chips.bet > chips.value:
            print("Sorry, you do not have enough chips to bet, please try again")
            continue
        else:
            break

    return chips.bet


def hit(hand, deck):
    '''Append card to hand'''
    hand.draw(deck.deal_card())
    hand.aces()


def hit_or_stand(hand, deck):
    '''Ask if hit or stand until stand, or bust'''
    global playing

    while True:
        x = input("Would you like to Hit or Stand? - ")

        if x[0].lower() == 'h':
            hit(hand, deck)
        elif x[0].lower() == 's':
            print("Player stands\nDealer's turn:\n")
            playing = False
        else:
            print("Sorry please try again.\n")
            continue
        break


def show_dealer_down(player, dealer):
    '''Show hands with one dealer card facing down'''
    print("Dealer's Hand: ")
    print(" <Card Hidden> ")
    print(dealer.cards[1])
    print("Player's Hand: ", *player.cards, sep='\n ')
    print(f"Player's hand = {player.value}")


def show_dealer_up(player, dealer):
    '''Show all of dealer's cards'''
    print("Dealer's Hand: ", *dealer.cards, sep='\n')
    print(f"Dealer's total = {dealer.value}")
    print("Player's Hand: ", *player.cards, sep='\n')
    print(f"Player's total = {player.value}")


def player_blackjack(player, chips):
    '''If player gets 21 on the draw, they get paid 2:1'''
    print("Player gets Blackjack!")
    chips.value += chips.bet * 2


def player_win(player, chips):
    '''If player wins, add winnings to value'''
    print("Player wins!")
    chips.win_bet()


def player_bust(player, chips):
    '''If player busts, subtract bet from value'''
    print("Player busts!")
    chips.lose_bet()


def dealer_win(player, chips):
    '''If dealer wins, subtract bet from value'''
    print("Dealer wins!")
    chips.lose_bet()


def dealer_bust(player, chips):
    '''If dealer busts, add winnings to value'''
    print("Dealer busts!")
    chips.win_bet()


def push():
    '''No winner'''
    print("No winner, this game is a push!")
