'''
This is the main Blackjack game file
'''

import cards as c

# script start
while True:
    # set game loops below
    playing = True
    split = False

    # create and shuffle deck
    my_deck = c.Deck()
    my_deck.shuffle()

    # ask player how many chips to buy on first loop, skip on subsequent loops
    try:
        if player_bank.value > 0:
            pass
    except:
        player_bank = c.Chips(0)
        c.ask_chips(player_bank)

    # ask if ready to play
    if not (c.ready_to_play()):
        print("Thanks for wasting my time! See you later!")
        break

    # game loop starts
    while playing:

        # ask player how much they want to bet

        while player_bank.bet == 0:
            c.ask_bet(player_bank)
            if player_bank.bet > player_bank.value:
                print("You do not have enough chips to bet this amount")
                player_bank.bet = 0
            else:
                print(f"You are betting {player_bank.bet} chips")
                break

        split_bank = c.Chips(0)

        # deal player and dealer's hands
        player = c.Hand()
        dealer = c.Hand()
        player_split = c.Hand()
        player_split.skip = True

        player.draw(my_deck.deal_card())
        dealer.draw(my_deck.deal_card())
        player.draw(my_deck.deal_card())
        dealer.draw(my_deck.deal_card())

        # show hands
        print("Dealer's Hand")
        print(" <Hidden Card> ")
        print(dealer.cards[1])

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
                player.skip = True

            # display split hand
            print("Split Hand")
            c.disp_hand(player_split)

            # hit/stand for split hand
            while not split_hand.skip:
                c.hit_or_stand(player_split, my_deck)
                print("\nSplit Hand")
                c.disp_hand(player_split)

                if player_split.bust == True:
                    c.player_bust(player_split, split_bank)
                    player_split.skip = True
                    split = False
                    break

            # exit split loop
            if player_split.value <= 21:
                print("Split Hand")
                c.disp_hand(player_split)
                split = False
            else:
                break

        # if no blackjack or split, ask player to hit or stand
        while True:
            if player.skip:
                break
            else:
                while not player.skip:
                    c.hit_or_stand(player, my_deck)
                    print("\nPlayer's Hand")
                    c.disp_hand(player)

                    if player.bust == True:
                        c.player_bust(player, player_bank)
                        player.skip = True
                        break
            break

        # dealer's turn
        if player.skip == True:
            pass
        else:
            c.dealer_draw(player, player_split, dealer, player_bank, my_deck)

        # calculate results and exit playing loop
        c.calc_results(player, player_bank, player_split, split_bank, dealer)

        playing = False
        break

    # show current bank amount and ask to play again
    if player_bank.value > 0:
        print(f"Your chip count current stands at - {player_bank.value}")
        again = input("Would you like to play again?(y/n) - ")

        if again[0].lower() == 'y':
            playing = True
            c.reset_board(player, player_split, dealer, my_deck)
        else:
            print("Thanks for playing! Sorry, the money isn't real.")
            break
    else:
        print("Sorry, you lost all of your money! Thanks for playing!")
        break
