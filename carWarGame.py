import random

class Card:

    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K':13, 'A':14}

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit
        self.value = Card.values[self.rank]

    def __str__(self) -> str:
        return f'{self.rank}{self.suit}{self.value}'


class Deck:

    ranks =  ['2', '3', '4', '5', '6', '7', '8', '9','10', 'J', 'Q', 'K', 'A']
    suits = ['♣','♦','♥','♠']

    def __init__(self):
       self.cards = self.generateDeck()


    def generateDeck(self) -> list:
        deck = []
        for suit in self.suits:
            for rank in self.ranks:
                card = Card(rank,suit)
                deck.append(card)
        return deck
    
    def showDeck (self):
        for card in self.cards:
            print(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def __str__(self) -> str:
        return f'{len(self.cards)}'
    

if __name__ == '__main__':
    deck = Deck()
    deck.showDeck()