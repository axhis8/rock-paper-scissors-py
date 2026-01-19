from rps import RockPaperScissors
import pytest

class TestRockPaperScissors:

    @pytest.mark.parametrize(
    "human, computer, expected", 
    [("scissors", "paper", "human"),
     ("paper", "rock", "human"),
     ("rock", "scissors", "human"),
     ("paper", "scissors", "computer"),
     ("rock", "paper", "computer"),
     ("scissors", "rock", "computer"),
     ("scissors", "scissors", "draw"),
     ("paper", "paper", "draw"),
     ("rock", "rock", "draw")])
    def test_check_win(self, human, computer, expected) -> None:
        game: RockPaperScissors = RockPaperScissors()
        assert game.check_win(human, computer) == expected