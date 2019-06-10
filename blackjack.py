'''
This is the main Blackjack game file
'''

import cards as c

my_deck = c.Deck()
my_deck.shuffle()

print(my_deck)

my_card = my_deck.deal_card()

print(my_card)
