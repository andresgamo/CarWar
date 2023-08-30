import random
import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__file__)


class Card:
    values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = Card.values[self.rank]

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"


class Deck:
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["♣", "♦", "♥", "♠"]

    def __init__(self) -> None:
        self.cards = self.generate_deck()
        self.length = len(self.cards)

    def generate_deck(self) -> list:
        """Generates a full deck of cards."""
        return [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def show_deck(self) -> None:
        """Shows in console the cards that are on the pit."""
        for card in self.cards:
            logger.info(card)

    def shuffle(self) -> None:
        """Shuffles the deck of cards"""
        random.shuffle(self.cards)

    def split(self) -> tuple:
        """Split cards in two equal parts"""
        return self.cards[: self.length / 2], self.cards[self.length / 2 :]

    def __str__(self) -> str:
        return self.length


class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def show_deck(self) -> None:
        """Displays all player's hand in console."""
        for card in self.cards:
            logger.info(card)

    def bet(self) -> Card:
        """Remove the top card from player's hand and return it"""
        return self.cards.pop(0)

    def add_cards(self, cards_pit: list) -> None:
        """Add cards from pit to the bottom of the player's hand"""
        for card in cards_pit:
            self.cards.append(card)

    def __str__(self) -> str:
        return f"{self.name.capitalize()} has {len(self.cards)} cards."


def greet_and_start() -> bool:
    """Diplay welcome message to players and ask whether want to start or exit."""

    options = {"1": True, "2": False}

    print("Welcome to CarWar game... Rise your bets!")

    while True:
        opt = input("Select an option:\n1. Start.\n2. Exit.\n").strip()
        if opt in options:
            return options[opt]
        else:
            print("Please enter valid option.")


def get_users_name() -> list:
    """Display message asking for user's name."""
    players_name = []

    for player in range(1, 3):
        while True:
            player_name = input(f"Player{player}, enter name (alphanum only): ")
            if player_name.isalnum():
                players_name.append(player_name)
                break
            else:
                print("Please enter valid name (alphanum only).")

    return players_name


if __name__ == "__main__":
    start = greet_and_start()
    if start:
        p1_name, p2_name = get_users_name()
        deck = Deck()
        player1, player2 = deal_and_player_instantiation(p1_name, p2_name, deck)
        print(player1, player2)
    else:
        print("Hope to see you soon.")

    # options = ['1','2']
    # while True:
    #     opt = input('Select an option:\n1. Enter name.\n2. Exit Game.')
    #     if opt in options:
    #         player1, player2 = ask_user_names()
    #         break
    #     else:
    #         print('Please enter valid option.')

    # deck = Deck()
    # deck.shuffle()
    # player1 = Player('player1',deck.cards[:int(len(deck.cards)/2)])
    # player2 = Player('player2',deck.cards[int(len(deck.cards)/2):])
    # player1.showDeck()
    # print(len(player1.cards))
    # print('\n')
    # player1.addCards([player1.bet()])
    # player1.showDeck()
    # print(len(player1.cards))
