from utilities import helpers
import datetime
import random
import importlib

importlib.reload(helpers)

"""
https://stackabuse.com/how-to-format-dates-in-python/
"""

##############################################################################################


GAME_DATA = {"username": None, "date": None, "score": None}


# TODO Read store data to append latest game information

def play_game():
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

            GAME_DATA["username"] = player
            GAME_DATA["date"] = date
            GAME_DATA["score"] = attempts

            # Save info in disk
            helpers.save_score(stored_score=GAME_DATA)
            break

        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")


##############################################################################################
# Test area
if __name__ == '__main__':
    play_game()
