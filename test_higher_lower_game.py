import pytest 
from higher_lower_game import HigherLower

class TestHigherLower:
    new_game_test_1 = HigherLower()
    def test_display_points(self):
        assert self.new_game_test_1.display_points() == 0
    def test_update_user_points(self):
        for _  in range(10):
            self.new_game_test_1.user_points = self.new_game_test_1.update_points()
        assert self.new_game_test_1.display_points() == 10

class TestDisplayData:
    new_game_test_2 = HigherLower()
    @pytest.mark.parametrize("who, name, description, country, text", [
        ("Compare A","Camila Cabello", "Musician", "Cuba", "Compare A: Camila Cabello, a Musician, from Cuba." ),
        ("Compare A", "Nasa", "Space agency", "United States", "Compare A: Nasa, a Space agency, from United States."),
        ("Against B","Lionel Messi","Footballer","Argentina","Against B: Lionel Messi, a Footballer, from Argentina.")
    ])
    def test_display_data(self, who, name, description, country, text):
        assert self.new_game_test_2.display_data(who, name, description, country) == text

class TestUnPackingData:
    new_game_test_3 = HigherLower()
    @pytest.mark.parametrize("data_dictionary, data_values",[
        ({
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States'}, ("Beyoncé", 145, "Musician", "United States")),
        ({
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    }, ("Kylie Jenner", 172, "Reality TV personality and businesswoman and Self-Made Billionaire", "United States")),
        ({
        'name': 'Kevin Hart',
        'follower_count': 89,
        'description': 'Comedian and actor',
        'country': 'United States'
    }, ("Kevin Hart", 89, "Comedian and actor", "United States"))
    ])
    def test_unpack_data(self, data_dictionary, data_values):
        for elem in data_values:
            assert elem in self.new_game_test_3.unpacking_data(data_dictionary)

class TestCheckUserGuess:
    new_game_test_4 = HigherLower()
    @pytest.mark.parametrize("user_guess, followers_count_a, followers_count_b, result", [
        ("A", 100, 84, ("You're Right! Current score: 1.", True)),
        ("B", 84, 100, ("You're Right! Current score: 2.", True)),
        ("B", 100, 70, ("Sorry, that's wrong. Final score: 2", False)),
        ("A", 65, 84, ("Sorry, that's wrong. Final score: 2", False)),
    ])
    def test_check_user_guess(self, user_guess, followers_count_a, followers_count_b, result):
        assert self.new_game_test_4.check_user_guess(user_guess, followers_count_a, followers_count_b) == result