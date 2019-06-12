'''
This is the main Blackjack game file
'''

import cards as c

# start game loop
while True:
    # set game loops below
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

        # show hands
        print("Dealer's Hand")
        c.disp_dealer(dealer)

        print("\n\nPlayer's Hand")
        c.disp_hand(player)

        # check for player blackjack
        if player.blackjack == True:
            c.reward_blackjack(chips)
            playing = False
            break

        # check for split
        c.check_split(player, player_bank)

        # if player choses to split, start split loop
            while split:
                player_split, split_bank = c.split_hand(
                    player, player_bank, my_deck)
                player.draw(my_deck.deal_card())

                # checks to see if player's new hand is blackjack
                if player.blackjack == True:
                    c.reward_blackjack(chips)

                # display split hand
                print("Split Hand")
                c.disp_hand(player_split)

                # hit/stand for split hand

        # check post split player1 blackjack again

        # if no blackjack or split, ask player to hit or stand

        # dealer's turn if players have not busted

        # results + winnings

    # ask if want to play again
    again = input("Would you like to play again?(y/n) - ")

    if again[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
