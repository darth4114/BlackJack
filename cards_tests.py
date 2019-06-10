import cards as c

my_deck = c.Deck()
my_deck.shuffle()

player = c.Hand()
dealer = c.Hand()

player.draw(my_deck.deal_card())
player.draw(my_deck.deal_card())


################
# test for dealing cards to a hand

# for card in player.cards:
#     print(card)

# print(f"value = {player.value}")
# print(f"aces = {player.aces}")


###############
# test for chip buy-in and betting

player_bank = c.Chips(0)
c.ask_chips(player_bank)


print(f"This statement is outisde of the method! {player_bank.value} chips")

c.ask_bet(player_bank)
