from blackjack_classes import *                        # models for game (Card, Deck, User, Player and Dealer)
from blackjack_logic import *                          # implements a whole turn for Player and Dealer

__author__ = 'Dan Beiter'

"""
File: blackjack.py
Author: Dan Beiter
Language: Python 3
Description: blackjack.py provides the main function of the program,
             whose primary purpose is to call functions in other files.
"""


def main():
    """
        Initializes variables and goes through both the player's turn
        and dealer's turn for a game of blackjack.

        Parameters:
        Returns:
            None (NoneType)
    """

    welcome()                                          # basic rules
    deck = Deck(list())                                # new deck
    player = Player(0, 0, list(), 0, 100, 0)           # new instance of Player
    dealer = Dealer(0, 0, list(), 0)                   # new instance of Dealer
    play_again = True

    while player.chips > 0 and play_again is True:     # while player has chips left and wishes to continue:
        get_chips_bet(player)                          # prompt player for how many chips he / she wishes to bet
        deck.get_deck(deck)                            # create / shuffle the deck
        player.reset_values()                          # set player's deck to empty list, and hard / soft values to 0
        dealer.reset_values()                          # do same for dealer
        insurance_bet = 0
        dealer_card = deck.get_next_card(deck)         # get dealer's face up card
        dealer.add_card(dealer_card)                   # add it to dealer's hand
        print("Dealer's face up card: " + str(dealer_card.name) + "\n")  # display this to player
        sleep(2)                                       # used as a pause

        # if dealer shows an Ace and player has chips left:
        if str(dealer_card.name).startswith('A') and player.chips != 0:
            insurance_bet = get_insurance(player.chips, player.chips_bet)  # ask if player wants to purchase insurance
            player.chips -= insurance_bet              # decrease from amount of chips

        dealer_card = deck.get_next_card(deck)         # get next card
        dealer.add_card(dealer_card)                   # add to dealer's hand (but don't show to player)

        print("Your face down cards:")
        # player card #1:
        player_card = deck.get_next_card(deck)         # now get player's two starting cards:
        player.add_card(player_card)
        print(str(player_card.name))
        # player card #2:
        player_card = deck.get_next_card(deck)
        player.add_card(player_card)
        print(str(player_card.name))
        sleep(3)

        player_choice = player_turn(player, deck)      # go through player's complete turn
        # if player did not get a five-card charlie, surrender the hand, nor bust:
        if not player_choice == 'c' and not player_choice == 'r' and not player_choice == 'b':
            dealer_turn(player, dealer, deck, dealer_card, insurance_bet)   # go through dealer's turn
        play_again = check_play_again(player.chips)    # prompt if player wishes to play another hand

    exit_program(player.chips)                         # calls ending function


if __name__ == '__main__':
    main()                                             # main function call
    exit()                                             # exit from program
