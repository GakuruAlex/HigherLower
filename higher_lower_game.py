import os
from game_data import data
from art import vs, logo
from random import randint
class HigherLower:
    user_points = 0
    _data_length = len(data)

    def display_points(self) -> int:
        """_Display current player points_

        Returns:
            int: _current player points_
        """
        return self.user_points

    def update_points(self) -> int:
        """_Update player points_

        Returns:
            int: _new player points_
        """
        return self.user_points + 1

    def display_data(self,who: str, name:str, description: str, country: str) -> str:
        """_Format games data for display_

        Args:
            who (str): _a string for compare or against_
            name (str): _name of the celebrity_
            description (str): _summary of who the celeb is_
            country (str): _country of origin of the celeb_

        Returns:
            str: _formatted string with all the celeb details_
        """
        return "{}: {}, a {}, from {}.".format(who,name, description, country)

    def generate_counter(self)-> int:
        """_Generate random int between 0 and length of data list_

        Returns:
            int: _generated integer_
        """
        return randint(0, self._data_length - 1)

    def unpacking_data(self, data: dict) -> tuple:
        """_Unpack data in the given dictionary_

        Args:
            data (dict): _A dictionary containing person info_

        Returns:
            tuple: _A tuple containing name, follower_count, description and country_
        """
        name, follower_count, description, country = data.values()
        return name, follower_count, description, country

    def check_user_guess(self, user_guess: str, followers_count_a: int, followers_count_b: int)-> tuple:
        """_check whether the user guessed the celebrity with more followers and increment player points if right_

        Args:
            user_guess (str): _Guess from user as a string_
            followers_count_a (int): _Number of celebrity A followers_
            followers_count_b (int): _Number of celebrity B followers_

        Returns:
            tuple: _Message to print to console and whether user is correct_
        """
        if user_guess == "A" and followers_count_a > followers_count_b:
                    self.user_points = self.update_points()
                    return f"You're Right! Current score: {self.display_points()}.", True
        elif user_guess == "B" and followers_count_b > followers_count_a:
                    self.user_points =self.update_points()
                    return f"You're Right! Current score: {self.display_points()}.", True
        else:
                    return f"Sorry, that's wrong. Final score: {self.display_points()}", False

    def get_user_guess(self) -> str:
        """_Ask the user for their guess_

        Returns:
            _str_: _player guess_
        """
        return input("Who has more followers ? Type 'A' or 'B' :").upper()



#Game logic
    def higher_lower_game(self):
        counter_a = self.generate_counter()
        counter_b = self.generate_counter()
        while True:
            if counter_a == counter_b:
                counter_b = self.generate_counter()
            else:
                break
        is_game_on = True
        display_data_a= data[counter_a]
        display_data_b = data[counter_b]

        while is_game_on:

                name_a, follower_count_a, description_a, country_a = self.unpacking_data(display_data_a)
                name_b, follower_count_b, description_b, country_b = self.unpacking_data(display_data_b)
                print(logo)
                if self.user_points > 0:
                    print(message)
                print(self.display_data("Compare A: ",name_a, description_a, country_a))
                print(vs)
                print(self.display_data("Against B: ", name_b, description_b, country_b))
                user_guess = self.get_user_guess()
                message, is_game_on =self.check_user_guess(user_guess, followers_count_a= follower_count_a, followers_count_b= follower_count_b)

                if not is_game_on:
                    print(message)
                    break
                else:
                    os.system("clear")
                    if follower_count_a > follower_count_b:
                        while True:
                            new_counter = self.generate_counter()
                            if new_counter != counter_a:
                                display_data_a, display_data_b = display_data_a, data[new_counter]
                                break
                    else:
                        while True:
                            new_counter_b = self.generate_counter()
                            if new_counter_b != counter_b:
                                display_data_a, display_data_b = display_data_b, data[new_counter_b]
                                break