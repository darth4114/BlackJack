import cards as c

my_deck = c.Deck()
my_deck.shuffle()

player = c.Hand()
dealer = c.Hand()

player.draw(my_deck.deal_card())
# dealer.draw(my_deck.deal_card())
player.draw(my_deck.deal_card())
# dealer.draw(my_deck.deal_card())

# player_bank = c.Chips(100)
# player_bank.bet = 40

################
# test for dealing cards to a hand

# c.disp_hand(player)
# print(f"aces = {player.aces}")

################
# test bust switch

# c.disp_hand(player)

# c.hit(player, my_deck)
# c.disp_hand(player)
# print(f"{player.bust}")
# c.hit(player, my_deck)
# c.disp_hand(player)
# print(f"{player.bust}")
# c.hit(player, my_deck)
# c.disp_hand(player)
# print(f"{player.bust}")



###############
# test for chip buy-in and betting

# player_bank = c.Chips(0)
# c.ask_chips(player_bank)


# print(f"This statement is outisde of the method! {player_bank.value} chips")

# c.ask_bet(player_bank)


##############
# test for hitting and counting values of cards

# c.disp_hand(player)
# print(f"aces = {player.aces}")

# c.hit_or_stand(player, my_deck)

# c.disp_hand(player)
# print(f"aces = {player.aces}")

##############
# check for Blackjack

# c.disp_hand(player)

# if player.value == 21:
#     print("Blackjack!!! You Win!")
# else:
#     pass

##############
# split check for same card value, and ask for split

# c.disp_hand(player)


# if c.values[player.cards[0].rank] == c.values[player.cards[1].rank] and player_bank.bet * 2 < player_bank.value:
#     x = input("Do you want to split? (y/n) - ")

#     if x[0] == 'y':
#         player_split, split_bank = c.split_hand(player, player_bank, my_deck)
#         player.draw(my_deck.deal_card())
#     else:
#         pass

# try:
#     print("Player's Split Hand", *player_split.cards, sep='\n')
#     print(f"value = {player_split.value}")
#     print(f"Player's Split Bank = {split_bank.value}")
# except:
#     pass
