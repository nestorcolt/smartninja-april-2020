import datetime
import json
import random
import os

##############################################################################################
# Globals
current_directory = os.getcwd()
file_name = "game_score.json"
full_path_to_file = os.path.join(current_directory, file_name)
##############################################################################################

# Read store score at start of the game
stored_score = []

with open(full_path_to_file, "r") as ninja_file_2:
    stored_score = json.loads(ninja_file_2.read())

"""
We read this info at the beginning so we can add more attempts to the previous store list
"""

##############################################################################################

# secret = random.randint(1, 30)
player = input("Enter your name: ")
attempts = 0
secret = 22

# Game start
while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        stored_score.append(attempts)  # Add to the list read from json the last number of attempts
        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

##############################################################################################

# stored data in json file after game
# Python sets
stored_score = list(set(stored_score))

with open(full_path_to_file, "w") as ninja_file_2:
    ninja_file_2.write(json.dumps(stored_score))

##############################################################################################
# Output message from code
print("Best Score: {}".format(min(stored_score)))

##############################################################################################
# ------------------------------------------
# And don't forget to eat your vegetables ;)
