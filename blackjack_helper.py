from time import *                                     # used for sleep()

__author__ = 'Dan Beiter'

"""
File: blackjack_helper.py
Author: Dan Beiter
Language: Python 3
Description: blackjack_helper.py implements helper functions for the program
             called in blackjack_logic.py.
"""


def welcome():
    """
        Welcomes player to game, providing basic overview of rules.

        Parameters:
        Returns:
            None (NoneType)
    """

    print("Welcome to blackjack!")
    sleep(3)
    print("The Turning Stone Casino has given you 100 chips to start you off.")
    sleep(4)
    print("The game is played with 1 deck and regular Vegas rules.")
    sleep(4)
    print("Shuffling cards...\n")
    sleep(3)
    print("At any time during your turn, type '(h)elp' to see blackjack rules.\n")
    sleep(4)


def check_play_again(chips):
    """
        Prompts user if they wish to play another hand or not.

        Parameters:
            chips (int) - number of chips player has left
        Returns:
            play_again (bool) - true if yes, false otherwise
    """

    print("You now have " + str(chips) + " chips.")
    play_again_check = 'invalid'
    # while user enters invalid input:
    while not play_again_check.startswith('y') and not play_again_check.startswith('n'):
        play_again_check = input("Play another round? (y for yes / n for no) ")
    print()
    return play_again_check.startswith('y')            # true if player entered yes


def get_chips_bet(player):
    """
        Gets number of chips player wishes to bet during this hand.

        Parameters:
            player (Player) - have to access player's chips
        Returns:
            None (NoneType)
    """

    player.chips_bet = 0
    # player must bet [1, number of chips] chips:
    while player.chips_bet < 1 or player.chips_bet > player.chips:
        try:
            player.chips_bet = int(input("How many chips would you like to wager? "))
        except ValueError:                             # user entered input that cannot be parsed
            pass


def get_insurance(chips, bet):
    """
        Prompts player if they wish to purchase insurance if dealer has an Ace.
        If dealer gets a blackjack, player receives 3:2 payout on their insurance bet.

        Parameters:
            chips (int) - number of chips player has
            bet (int) - number of chips player placed on their main bet
        Returns:
            insurance_bet (int) - number of chips player bets (0 if none)
    """

    insurance_check = 'invalid'
    # prompt player if they wish to buy insurance against a dealer Ace
    while not insurance_check.startswith('y') and not insurance_check.startswith('n'):
        insurance_check = input("Make an insurance bet? (Pays 2:1) (y for yes / n for no) ")
    print()
    if insurance_check.startswith('y'):               # if so:
        insurance_bet = 0
        temp_chips = chips - bet
        print("You have " + str(temp_chips) + " chips left after initial bet.")  # display chips left after main bet
        while insurance_bet < 1 or insurance_bet > temp_chips:
            insurance_bet = int(input("How big of an insurance bet? "))
        return insurance_bet


def dealer_hit(dealer, player):
    """
        Checks if dealer will hit on the next move or stand.

        Parameters:
            dealer (Dealer) - must access dealer's current hand
            player (Player) - must access player's current hand
        Returns:
            dealer_hits (bool) - true if player is currently beating dealer; false otherwise
    """

    dealer_val = max(dealer.hard, dealer.soft)
    player_val = max(player.hard, player.soft)
    return dealer_val < player_val                    # if player beats dealer, dealer hits (house rules)


def exit_program(chips):
    """
        Provides a closing function for the player,
        letting them know if they ended up winning or losing chips on the whole.

        Parameters:
            chips (int) - number of chips player has when exiting the casino
        Returns:
            None (NoneType)
    """

    if chips == 0:                                    # player is broke
        print("You are all out of chips. Please come again.")
        return
    elif chips == 100:                                # broke even
        print("You have exited the casino with the same amount of chips you started with.")
        return
    if chips > 100:                                   # player made profit
        print("You have exited the casino with " + str(chips - 100) + " more chips.")
        return
    print("You have exited the casino with " + str(100 - chips) + " less chips.")  # player lost chips
