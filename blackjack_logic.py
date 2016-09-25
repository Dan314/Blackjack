# system imports:
import math                                            # used for ceiling (ceil) and floor functions
import webbrowser                                      # used for opening wikipedia article on blackjack

# custom import:
from blackjack_helper import *                         # used for dealer_hit function

__author__ = 'Dan Beiter'

"""
File: blackjack_logic.py
Author: Dan Beiter
Language: Python 3
Description: blackjack_logic.py provides the main logic for the game,
             both looping through user input and determining
             decisions of the dealer (CPU).
"""


def hit(player, deck):
    """
        Draws a card from the deck, adds it to the player's hand,
        and displays the card and the player's new hand value.

        Parameters:
            player (Player) - player to add cards to
            deck (Deck) - deck containing cards
        Returns:
            None (NoneType)
    """

    card_taken = deck.get_next_card(deck)              # get next card from deck
    print("Dealer deals: " + str(card_taken.name))     # display to user
    player.add_card(card_taken)                        # add to hand
    player.display_value("Your")                       # display player's current hand's value


def player_turn(player, deck):
    """
        Provides functionality like a switch statement in Java
        that loops until player busts or makes a final decision (e.g. surrender hand, double down...)

        Parameters:
            player (Player) - player makes decisions on whether to hit, stand, etc.
            deck (Deck) - deck containing cards to draw from
        Returns:
            player choice (char) - character representing if player (b)usted, su(r)rendered, etc.
    """

    while player.hard <= 21:                           # while player has not busted:
        if len(player.hand) == 5:                      # five card charlie
            print("5 card charlie; you win!")
            player.chips += player.chips_bet           # add to chips
            return 'c'                                 # return to main function
        else:
            hit_or_stand = input("Press enter to hit, d to double, r to surrender, anything else to stand: ")
            if hit_or_stand == '':                     # player hits:
                hit(player, deck)
            elif str(hit_or_stand).startswith('r'):    # surrender:
                print("You surrendered the hand, and get half your chips bet back.")
                player.chips -= math.ceil(player.chips_bet / 2)  # player loses half of chip bet
                return 'r'
            elif str(hit_or_stand).startswith('d'):    # double:
                if (player.chips - player.chips_bet) >= player.chips_bet:  # if player has enough to perform operation:
                    player.chips_bet *= 2              # double bet chips
                    hit(player, deck)                  # hit one more card
                    return 'd'
                else:
                    print("Not enough chips to double.\n")                 # not enough to double
                    pass
            elif str(hit_or_stand).startswith('h'):    # help:
                webbrowser.open('http://en.wikipedia.org/wiki/Blackjack')  # open wikipedia article
            else:                                      # stand:
                return 's'
    print("You busted!")                               # player hand value > 21
    player.chips -= player.chips_bet                   # lose bet
    return 'b'


def dealer_turn(player, dealer, deck, dealer_card, insurance_bet):
    """
        Dealer hits until he / she has a higher hand value than player,
        or until they bust. Dealer cannot double nor surrender hand.

        Parameters:
            player (Player) - dealer can compare hand values with the player
            dealer (Dealer) - update dealer object as dealer makes decisions
            deck (Deck) - deck containing cards
            dealer_card (Card) - player is shown dealer's face-down card
            insurance_bet (int) - number > 0 if player made insurance; 0 otherwise
        Returns:
            None (NoneType)
    """

    print()
    print("Dealer's face down card: " + str(dealer_card.name))  # display dealer's face-down card
    dealer.display_value("Dealer's")                   # dealer's hand's value
    sleep(2.5)

    if dealer.soft == 21:                              # dealer blackjack trumps player blackjack (house rules)
        print("Dealer got a blackjack", end='')
        if not insurance_bet == 0:                     # if player placed an insurance bet:
            print(", but you win insurance bet.")
            player.chips += (insurance_bet * 2)        # player wins this side bet
        player.chips -= player.chips_bet               # but loses main bet
        print("\n")
        sleep(1.5)
        return
    if player.soft == 21:
        print("You got blackjack! (Pays 3:2)")         # player blackjack pays 3 to 2
        player.chips += math.floor(player.chips_bet * 1.5)  # add to chips
        sleep(2.5)
        return

    print("Dealer now getting hand")
    while dealer.hard <= 21 and dealer_hit(dealer, player):  # while dealer did not bust and has not beaten player:
        print()
        sleep(3.5)
        dealer_card = deck.get_next_card(deck)         # get next card
        print("Dealer deals: " + str(dealer_card.name))
        dealer.add_card(dealer_card)                   # dealer hits
        dealer.display_value("Dealer's")
    print()
    sleep(2.5)

    if dealer.hard > 21:                               # if dealer busted:
        print("Dealer busted! Nice hand")
        player.chips += player.chips_bet               # player wins
    elif dealer.soft == 21:                            # dealer gets 21 (not blackjack)
        print("Dealer got a 21! Tough luck")
        player.chips -= player.chips_bet
    else:                                              # dealer's hand ties or beats player's
        print("Dealer got " + str(dealer.soft) + "; you lose this round")
        player.chips -= player.chips_bet
