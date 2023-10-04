import pytest
from pytest_mock import mocker
from card_war_game import Game, Deck


@pytest.fixture
def game_instance(mocker) -> Game:
    mocker.patch("card_war_game.Game.get_num_players", return_value=3)
    mocker.patch(
        "card_war_game.Game.get_users_name", return_value=["test1", "test2", "test3"]
    )
    mocker.patch.object(Deck, "shuffle")
    game = Game()
    return game


def test_init(game_instance):
    game = game_instance
    game.deck.shuffle.assert_called_once()
    assert game.num_players == 3
