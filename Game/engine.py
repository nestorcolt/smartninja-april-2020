from utilities import helpers
import datetime
import random
import importlib

importlib.reload(helpers)


##############################################################################################

class GameEngine:

    def __init__(self):
        self.game_data = {"username": None, "date": None, "score": None}

        # Method calls
        self.init_score_data_structure()

    def init_score_data_structure(self):
        data = helpers.load_score()
        if not data:
            helpers.save_score(stored_score=[])

    def update_score_data(self, new_data=None):
        data = helpers.load_score()
        data.append(new_data)
        helpers.save_score(stored_score=data)

    def play_game(self):
        player = input("Enter your name: ")
        # secret = random.randint(1, 30)
        secret = 22
        attempts = 0

        # Game start
        while True:
            guess = int(input("Guess the secret number (between 1 and 30): "))
            attempts += 1

            if guess == secret:
                time_now = datetime.datetime.now()
                date = time_now.strftime("%b %d %Y %H:%M:%S")

                self.game_data["username"] = player
                self.game_data["date"] = date
                self.game_data["score"] = attempts

                # Save info in disk
                self.update_score_data(new_data=self.game_data)
                break

            elif guess > secret:
                print("Your guess is not correct... try something smaller")
            elif guess < secret:
                print("Your guess is not correct... try something bigger")


##############################################################################################
# Test area
if __name__ == '__main__':
    engine = GameEngine()
    engine.play_game()
