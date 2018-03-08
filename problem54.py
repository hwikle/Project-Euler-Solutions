# Problem54.py
# Hank Wikle
# Last modified 7 February 2018
#
# This program solves Problem 54 on Project Euler (Poker Hands).
# The core of the program centers on two functions.
# The first of these functions determines the value of a hand.
# The second of these functions ranks one hand against another.
# This program depends on the file poker.txt, which can be found in the project_euler directory

# Functions

def is_flush(hand):
"""Determines whether the given hand is a flush. Returns a boolean."""
	suit = hand[0][1]

	for card in hand[1:]:
		if card[1] != suit:
			return False

	return True

def is_straight(hand):
"""Determines whether the given hand is a straight. Returns a boolean."""
	pass

def is_royal(hand):
"""Determines whether the given hand is a royal flush. Assumes the hand is a straight flush. Returns a boolean."""
	pass

def count_duplicates(hand):
"""Determines the highest number of duplicates in the given hand. Can be used on a hand of fewer than five cards. Returns a boolean."""
	pass

def eval_hand(cards):
	"""This function assigns a value (e.g. "flush") to a set of cards. Takes a list of strings as input. Returns a string."""

	pass

def rank_hands(hand1, hand2):
	"This function determines which of two hands outranks the other. Takes two strings (e.g. "flush"). Returns a string (e.g. "player 1", "tie"). Assumes hand1 belongs to player 1 and hand2 belongs to player 2."""

	pass

# Classes

class Card(object):
"""Defines the card class"""

	def __init__(self, name):
	"Initializes the Card class. Assumes name is a string of form "AH" (Ace of Hearts)."""
		self.value = name[0]
		self.suit = name[1]

	def __lt__(self, other):
		pass
	def __gt__(self, other):
		pass
