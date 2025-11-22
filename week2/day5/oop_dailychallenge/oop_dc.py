#Daily challenge: OOP Quizz

#Exercise 1: Quizz
# Answer the following questions:

# What is a class? 
# a class is like a blueprint for creating objects. 
# It defines the structure and behavior that objects of that type will possess.

# What is an instance?
#is a specific object created from a class.

# What is encapsulation?
# It is when we can restrict access to methods and variables. 
# This prevents data from direct modification, which is called encapsulation. 
# In Python, we denote private attributes using underscore as prefix i.e., single _ or double

# What is abstraction?
#is the process of simplifying complex systems by hiding unnecessary
# implementation details and revealing only the essential features to the user. 
# It focuses on "what" an object does rather than "how" it achieves its functionality

# What is inheritance?
#is a mechanism in which one class acquires the property of another class.

# What is multiple inheritance?
#it happens when one class gets the properties from different classes.

# What is polymorphism?
#the ability of an object to take on many forms. It allows you to use a single 
# interface to represent different underlying types of objects, 
# enabling more flexible and reusable code.

# What is method resolution order or MRO?
#it iss the sequence in which a programming language searches for a method or
#  attribute in a class hierarchy, especially when using multiple inheritance.

#Exercise 2: Create a deck of cards class
#The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

import random

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'{self.value} of {self.suit}' 
    
class DeckOfCards():
    def __init__(self):
        self.cards = []
        self.shuffle() 

    def shuffle(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = []
        for suit in suits:
            for value in values:
                card = Card(suit,value)
                self.cards.append(card)             
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

deck = DeckOfCards()
print(deck.deal())         
print(len(deck.cards))    
print(deck.deal())  
print(deck.deal())  
print(deck.deal())  
print(len(deck.cards)) 