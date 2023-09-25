import random
import logging
import time

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

    def split(self, num_players) -> tuple[Card]:
        """Split cards in two equal parts"""
        hands = []
        hand_size = len(self) // num_players
        for _ in range(num_players):
            hands.append(self.cards[:hand_size])
            del self.cards[:hand_size]
        return hands

    def __str__(self) -> str:
        return f"{len(self)}"

    def __len__(self) -> int:
        return len(self.cards)


class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards: list[Card] = cards
        self.current_bet: None | Card = None

    def show_deck(self) -> None:
        """Displays all player's hand in console."""
        for card in self.cards:
            logger.info(card)

    def bet(self) -> Card:
        """Remove the top card from player's hand and return it"""
        self.current_bet = self.cards.pop(0)
        return self.current_bet

    def add_cards(self, cards_pit: list) -> None:
        """Add cards from pit to the bottom of the player's hand"""
        for card in cards_pit:
            self.cards.append(card)

    def __str__(self) -> str:
        return f"{self.name.capitalize()} has {len(self)} cards."

    def __len__(self) -> int:
        return len(self.cards)


class Game:
    def __init__(self) -> None:
        self.num_players = self.get_num_players()
        self.players_name = self.get_users_name()
        logger.info("\nGame is above to start!")
        time.sleep(3)
        self.deck = Deck()
        self.deck.shuffle()
        self.players_hand = self.deck.split(self.num_players)
        self.players = self.create_players()
        self.active_players = self.players
        self.pit = []
        logger.info(self)

    def get_num_players(self) -> int:
        """Display message asking for the num of players from 2 to 4."""
        while True:
            num_players = input("Please enter number of players (2-4): ").strip()
            if num_players.isdigit() and num_players in ["2", "3", "4"]:
                return int(num_players)
            else:
                logger.warning("Please enter valid number of players")

    def get_users_name(self) -> list[str]:
        """Display message asking for user's name."""
        players_name = []

        for player in range(1, self.num_players + 1):
            while True:
                player_name = input(f"Player{player}, enter name (alphanum only): ")
                if player_name.isalnum():
                    players_name.append(player_name)
                    break
                else:
                    logger.warning("Please enter valid name (alphanum only).")

        return players_name

    def create_players(self) -> list[Player]:
        """Instaciate players"""
        return [
            Player(name, cards)
            for name, cards in zip(self.players_name, self.players_hand)
        ]

    def bet(self) -> list[Card]:
        """Return current players bet"""
        return [player.bet() for player in self.active_players]

    def add_to_pit(self, cards: list[Card]) -> None:
        """Add cards to pit"""
        self.pit.extend(cards)

    def end(self) -> bool:
        """Eval if any player win."""
        if self.num_players == 3:
            return any(len(player) >= 35 for player in self.players)
        else:
            return any(len(player) >= 26 for player in self.players)

    def show_bets(self) -> None:
        """Displays players bets"""
        for player in self.active_players:
            logger.info("%s - %s", player.name, player.current_bet)

    def is_war(self) -> bool:
        """Eval condition of war"""
        # current_bets = self.get_current_bets()
        # return current_bets.count(self.get_highest_bet()) > 1
        return isinstance(self.get_highest_bet_player(), list)

    def add_winner_cards(self) -> Player:
        """Add cards to winner's hand and return the winner"""
        winner = self.get_highest_bet_player()
        winner.add_cards(self.pit)
        return winner

    # def get_current_bets(self) -> list[int]:
    #     """Return players current bet value"""
    #     return [player.current_bet.value for player in self.players]

    def get_highest_bet(self) -> Card:
        """Return the value of the highest card from players current bets"""
        # player = self.get_highest_bet_player()
        # return player.current_bet.value
        return max(player.current_bet.value for player in self.active_players)

    def get_highest_bet_player(self) -> Player | list[Player]:
        """Return the player with the highest bet.
        In case of concurrency return all players within the condition."""
        # highest_bet = max(self.players, key=lambda player: player.current_bet.value)
        highest_bet = self.get_highest_bet()
        highest_bet_players = [
            player
            for player in self.active_players
            if highest_bet == player.current_bet.value
        ]
        return (
            highest_bet_players
            if len(highest_bet_players) > 1
            else highest_bet_players[0]
        )

    def update_active_players(self) -> None:
        """Update the self.active_players attribute with the players
        who still have cards in their hand."""
        self.active_players = [player for player in self.players if len(player) > 0]

    def __len__(self):
        return self.num_players

    def __str__(self) -> str:
        players_str = "\n".join(map(str, self.players))
        return f"There are {self.num_players} players in the game:\n{players_str}"


def greet_and_start() -> bool:
    """Diplay welcome message to players and ask whether want to start or exit."""

    options = {"1": True, "2": False}

    logger.info("Welcome to CarWar game... Rise your bets!")

    while True:
        opt = input("Select an option:\n1. Start.\n2. Exit.\n").strip()
        if opt in options:
            return options[opt]
        else:
            logger.warning("Please enter valid option.")


def play() -> None:
    """Encloses the whole game program"""
    start = greet_and_start()
    if start:
        game = Game()
        while not game.end():
            game.add_to_pit(game.bet())
            game.show_bets()
            if game.is_war():
                logger.info('War')
                game.update_active_players()
            else:
                logger.info(game.add_winner_cards())
                game.pit = []
                winner = game.get_highest_bet_player()
                winner.show_deck()
                game.update_active_players()
        logger.info("WINNER!: %s\n%s", winner.name, winner)
    else:
        logger.info("Hope to see you soon.")


if __name__ == "__main__":
    play()
