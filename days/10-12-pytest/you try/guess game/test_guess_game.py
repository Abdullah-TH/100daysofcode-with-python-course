from unittest.mock import patch
import pytest
import random
from guess_game import get_random_number
from guess_game import Game


@patch.object(random, "randint")
def test_get_random_number(m):
    m.return_value = 10
    assert 10 == get_random_number()


@patch(
    "builtins.input",
    side_effect=[11, 12, "bob", 12, 5, -1, 20, 21, None]
)
def test_guess(input_value):
    game = Game()
    assert game.guess() == 11
    assert game.guess() == 12
    _pytest_raises_value_error_for(game)
    _pytest_raises_value_error_for(game)
    assert game.guess() == 5
    _pytest_raises_value_error_for(game)
    assert game.guess() == 20
    _pytest_raises_value_error_for(game)
    _pytest_raises_value_error_for(game)


def test_check_guess(capfd):
    game = Game()
    game._answer = 3

    assert not game._check_guess(1)
    _assert_output(capfd, "1 is too low")

    assert not game._check_guess(2)
    _assert_output(capfd, "2 is too low")

    assert not game._check_guess(4)
    _assert_output(capfd, "4 is too high")

    assert game._check_guess(3)
    _assert_output(capfd, "3 is correct!")


@patch(
    "builtins.input",
    side_effect=[4, 22, 9, 4, 6]
)
def test_game_win(input_value):
    game = Game()
    game._answer = 6
    game()
    assert game._win


@patch(
    "builtins.input",
    side_effect=[4, 22, 9, 5, 6]
)
def test_game_lose(input_value):
    game = Game()
    game._answer = 7
    game()
    assert not game._win


@patch(
    "builtins.input",
    side_effect=[1, 2, 3, 4, 5, 6]
)
def test_game_maximum_5_guesses(input_value):
    game = Game()
    game._answer = 6
    game()
    assert not game._win


@patch(
    "builtins.input",
    side_effect=[1, 1, None, "Abdullah", 2, 3, 4, 5]
)
def test_game_error_inputs_not_counted(input_value):
    game = Game()
    game._answer = 5
    game()
    assert game._win


def _pytest_raises_value_error_for(game: Game):
    with pytest.raises(ValueError):
        game.guess()


def _assert_output(capfd, output):
    out, _ = capfd.readouterr()
    assert out.strip() == output
