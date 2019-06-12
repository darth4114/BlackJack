'''
This is the main Blackjack game file
'''

import cards as c

playing = True
split = False

# create and shuffle deck
my_deck = c.Deck()
my_deck.shuffle()

# ask player how many chips to buy
player_bank = c.Chips(0)
c.ask_chips(player_bank)

# game loop starts
while playing:

    # ask if ready to play
    c.ready_to_play()

    # ask player how much they want to bet
    c.ask_bet(player_bank)

    # deal player and dealer's hands
    player = c.Hand()
    dealer = c.Hand()

    player.draw(my_deck.deal_card())
    dealer.draw(my_deck.deal_card())
    player.draw(my_deck.deal_card())
    dealer.draw(my_deck.deal_card())

    # check for player blackjack
    c.check_blackjack(player, player_bank)

    # check for split
    c.check_split(player, player_bank)

    # if player choses to split, start split loop
        while split:
            player_split, split_bank = c.split_hand(
                player, player_bank, my_deck)
            player.draw(my_deck.deal_card())

            c.check_blackjack(player, player_bank)

# ask if want to play again
