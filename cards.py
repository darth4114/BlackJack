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
        self.bust = False

    def draw(self, card):
        '''Drawing card from Deck() and adding value to total'''
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        if self.value > 21:
            self.bust = True

    def ace_adjust(self):
        '''Compensate for aces if cards are over 21'''
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            self.bust = False

    def split(self):
        '''Split hand if cards are same value'''
        self.value -= values[self.cards[0].rank]
        return self.cards.pop()


def disp_hand(player):
    print(f"Player's Hand", *player.cards, sep='\n')
    print(f"Hand Value = {player.value}")


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


def ask_chips(chips):
    '''Asks player how many chips they want to start with'''
    while True:
        try:
            chips.value = int(input("How many chips do you want to buy? - "))
        except ValueError:
            print("Sorry, I didn't understand you, please try again")
            continue
        else:
            if chips.value < 1:
                print(
                    "You haven't bought enough chips to play, you need to purchase more.\n")
                continue
            else:
                break

    print(f"Thank you!\nYou have bought {chips.value} chips!")


def ask_bet(chips):
    '''Asks player for a bet, cannot be more than their current chip count'''
    while True:
        try:
            chips.bet = int(input("How many chips do you want to bet? - "))
        except ValueError:
            print("Sorry, I didn't understand you, please try again")
            continue
        else:
            if chips.bet > chips.value:
                print("Sorry, you do not have enough chips to bet, please try again")
                continue
            else:
                break

    print(f"You are betting {chips.bet} chips")


def split_hand(hand, chips, deck):
    '''
    return a new hand of a popped card from the player's hand, and a card from the desk
    also returns a new bank with the player's bet as the value and bet values
    '''
    global split

    play_split = Hand()
    play_split.draw(hand.split())
    play_split.draw(deck.deal_card())

    bank_split = Chips(chips.bet)
    bank_split.bet = chips.bet
    chips.value -= chips.bet

    check_blackjack(play_split, bank_split)

    return play_split, bank_split


def hit(hand, deck):
    '''Append card to hand'''
    hand.draw(deck.deal_card())
    hand.ace_adjust()


def hit_or_stand(hand, deck):
    '''Ask if hit or stand until stand, or bust'''
    global playing

    while True:
        x = input("Would you like to Hit or Stand? - ")

        if x[0].lower() == 'h':
            hit(hand, deck)
        elif x[0].lower() == 's':
            print("Player stands\n turn:\n")
            playing = False
        else:
            print("Sorry please try again.\n")
            continue
        break


def ready_to_play():
    '''Ask player if they want to play'''
    global playing

    x = input("Are you ready to play?(y/n) - ")

    if x[0].lower() == 'y':
        continue
    else:
        print("Thanks for playing!")
        playing = False


def check_blackjack(hand, chips):
    '''Check if the player has blackjack and stop game if blackjack'''
    global playing

    if hand.value == 21:
        print("Player gets Blackjack!")
        chips.value += chips.bet * 2
        playing = False
    else:
        continue

    # needs something to check if the function is nested or not, if nested, then execute split = False code on blackjack


def check_split(hand, chips):
    '''Check if the player's deal and bank are eligible for a split hand'''
    global split

    if values[hand.cards[0].rank] == values[hand.cards[1].rank] and chips.bet * 2 < chips.value:
    x = input("Do you want to split? (y/n) - ")

        if x[0] == 'y':
            print("Splitting hand!")
            split = True
        else:
            print("Hand will not be split")


def push():
    '''No winner'''
    print("No winner, this hand is a push!")


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


def split_combine(chips, split, sp_chips, dealer):
    '''Combine winnings/losses from a split hand'''
    if split.bust = True or dealer.value > split.value:
        continue
    elif:
        split.value > dealer.value:
        hips.value += sp_chips.bet


def play_again():
    '''Ask if they player wants to play again'''
    global playing

    x = input("Would you like to play again?(y/n) - ")

    if x[0].lower() == 'y':
        playing = True
    else:
        print("Thanks for playing!")
        playing = False
