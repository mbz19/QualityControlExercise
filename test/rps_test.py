
from app.rps import determine_winner


def test_example():
    assert 2 + 2 == 4



def test_winnters():
    assert determine_winner(u="rock", c="scissors") == "USER WINS"
    assert determine_winner(u="rock", c="paper") == "COMPUTER WINS"
    assert determine_winner(u="rock", c="rock") == "TIE GAME"

    assert determine_winner(u="paper", c="rock") == "USER WINS"
    assert determine_winner(u="paper", c="scissors") == "COMPUTER WINS"
    assert determine_winner(u="paper", c="paper") == "TIE GAME"

    assert determine_winner(u="scissors", c="paper") == "USER WINS"
    assert determine_winner(u="scissors", c="rock") == "COMPUTER WINS"
    assert determine_winner(u="scissors", c="scissors") == "TIE GAME"

#you might have test functions here 