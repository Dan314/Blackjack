import random                                          # used for shuffling the deck

__author__ = 'Dan Beiter'

"""
File: blackjack_classes.py
Author: Dan Beiter
Language: Python 3
Description: blackjack_classes.py provides the necessary models for the program,
             including classes for a Card, Deck, User, Player (subclass of User)
             and Dealer (also subclass of User)
"""


class Card:                                            # represents a card in the deck
    def __init__(self, name, value):                   # constructor
        self.name = name                               # e.g. King of Diamonds
        self.value = value                             # e.g. 7


class Deck:                                            # represents a deck of 52 cards
    face_cards = ['Jack', 'Queen', 'King']             # Ace is kept separate
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']  # card suits

    def __init__(self, cards):                         # constructor
        self.cards = cards

    @staticmethod
    def get_deck(self):
        """
            Creates and shuffles the deck of cards to be used in a game.

            Parameters:
                self (Deck) - the deck object referred to
            Returns:
                deck (Deck) - the 52-card deck
        """

        self.cards = list()                            # create empty list
        for suit in self.suits:                        # for each suit:
            self.cards.append(Card('Ace' + ' of ' + suit, 1))  # add Ace of said suit
            for num in range(2, 11):                   # as well as 2 through 10 (11 excluded)
                self.cards.append(Card(str(num) + ' of ' + str(suit), num))
            for face in self.face_cards:               # and Jack, Queen and King
                self.cards.append(Card(face + ' of ' + str(suit), 10))

        random.shuffle(self.cards)                     # shuffle the deck (pseudo-)randomly
        return self.cards                              # return deck

    @staticmethod
    def get_next_card(self):
        """
            Pops and returns the top card off the deck.

            Parameters:
                self (Deck) - deck to pop from
            Returns:
                card (Card) - the next card to be utilized in game
        """

        return self.cards.pop(0)                       # pop off top card from (shuffled) deck


class User:                                            # represents a User (either Player or Dealer)
    soft = 0                                      # hand value counting as many Aces as 11's as possible without busting
    hard = 0                                           # hand value counting Aces as 1's
    hand = list()                                      # no cards in hand to begin with
    soft_aces = 0                                      # number of Aces counted as 11 in soft value (can be 0 or 1 only)

    def __init__(self, soft, hard, hand, soft_aces):   # constructor
        self.soft = soft
        self.hard = hard
        self.hand = hand
        self.soft_aces = soft_aces

    def add_card(self, card):
        """
            Adds a card to a user's hand and updates their hand value.

            Parameters:
                self (User) - user object to add card to
                card (Card) - card to add
            Returns:
                None (NoneType)
        """

        self.hand.append(card)                         # add card to player's or dealer's hand
        self.hard += card.value                        # adjust hard and soft values accordingly (Aces as 1)
        self.soft += card.value
        if card.name[0:3] == 'Ace' and self.soft_aces == 0:  # if card is an Ace:
            self.soft += 10                            # count card as 11 in soft value
            self.soft_aces = 1                         # iterate number of Aces counted as 11 by 1
        if self.soft > 21 and self.soft_aces == 1:     # if player's soft value is over 21 and an Ace counts as 11:
            self.soft -= 10                            # change to value of 1
            self.soft_aces = 0

    def display_value(self, user_type):
        """
            Displays the hard / soft values of a user's hand
            depending on the types of cards they have in their hand.

            Parameters:
                self (User) - user with a hand of cards
                user_type (string) - represents user type when displaying information
            Returns:
                None (NoneType)
        """

        if self.hard == self.soft:                     # value is the same; only display one
            print(user_type + " current hand total: " + str(self.hard) + "\n")
        else:                                          # display both hard and soft values of user
            print(user_type + " current hand total: hard " + str(self.hard)
                  + "; soft " + str(self.soft) + "\n")

    def reset_values(self):
        """
            Rests soft / hard hand values, list of cards and soft ace count.

            Parameters:
                self (User) - user to reset statistics for
            Returns:
                None (NoneType)
        """

        self.soft = 0
        self.hard = 0
        self.soft_aces = 0
        self.hand = list()


class Player(User):
    chips = 100                                        # initial number of chips upon entering casino

    def __init__(self, soft, hard, hand, soft_aces, chips, chips_bet):  # constructor
        super().__init__(soft, hard, hand, soft_aces)  # call super() for constructor in parent User class
        self.chips = chips                             # then set variables unique to a Player instance
        self.chips_bet = chips_bet


class Dealer(User):
    def __init__(self, soft, hard, hand, soft_aces):   # constructor
        super().__init__(soft, hard, hand, soft_aces)  # no extra params for Dealer class
