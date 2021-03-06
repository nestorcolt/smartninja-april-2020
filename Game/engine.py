from utilities import helpers
import datetime
import random
import importlib

importlib.reload(helpers)

"""
CRUD Methodology
https://en.wikipedia.org/wiki/Create,_read,_update_and_delete
"""


##############################################################################################

class GameEngine:

    def __init__(self):
        self.game_data = {"username": None, "date": None, "score": None}
        self.current_statistics = None
        self.secret_number = random.randint(1, 30)
        self.player = None
        self.attempts = 0

        # Method calls
        self.init_score_data_structure()

    def init_score_data_structure(self):
        data = helpers.load_score()
        if not data:
            data = []
            helpers.save_score(stored_score=data)

        self.current_statistics = data

    def get_player_name(self, player_name="JohnDoe"):
        self.player = player_name

    def update_score_data(self, new_data=None):
        self.current_statistics.append(new_data)
        helpers.save_score(stored_score=self.current_statistics)

    def get_best_player(self, data):
        scores = []
        players = []

        for player_info in data:
            score = player_info["score"]
            scores.append(score)

        min_score_value = min(scores)

        for player_info in data:
            score = player_info["score"]
            if score == min_score_value:
                players.append(player_info)

        dates = []

        for player in players:
            date = self.get_real_date_from_string(player["date"])
            dates.append(date)

        recent = max(dates)
        recent = recent.strftime("%b %d %Y %H:%M:%S")

        for player in players:
            if player["date"] == recent:
                return player

    def show_statistics(self):
        data = self.get_best_player(data=self.current_statistics)

        message = """
            Player : {}
            Best Score: {}
            date: {}
        """.format(data["username"].lower().capitalize(),
                   data["score"],
                   data["date"])

        output = "Best player info:\n{}".format(message)
        print(output)
        return output

    def get_real_date_from_string(self, date):
        datetime_object = datetime.datetime.strptime(date, "%b %d %Y %H:%M:%S")
        return datetime_object

    def play_game(self, guess):

        # Game start
        self.attempts += 1

        if guess == self.secret_number:
            time_now = datetime.datetime.now()
            date = time_now.strftime("%b %d %Y %H:%M:%S")

            self.game_data["username"] = self.player
            self.game_data["date"] = date
            self.game_data["score"] = self.attempts

            # Save info in disk
            self.update_score_data(new_data=self.game_data)

            # Show game statistics
            result = self.show_statistics()
            return result

        elif guess > self.secret_number:
            return "Your guess is not correct... try something smaller"
        elif guess < self.secret_number:
            return "Your guess is not correct... try something bigger"

##############################################################################################
