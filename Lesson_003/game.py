import random
import os

##############################################################################################
current_directory = os.getcwd()
file_name = "game_score.txt"
full_path_to_file = os.path.join(current_directory, file_name)
##############################################################################################

# secret = random.randint(1, 30)
secret = 22
attempts = 0

player = input("Enter your name: ")

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

# We want to store last game data in a txt file [user, attempts]
# string data to store
string_to_store = "Player Name: {} - Attempts: {}".format(player, attempts)
#
with open(full_path_to_file, "w") as ninja_file_2:
    ninja_file_2.write(string_to_store)

##############################################################################################
# Output the game latest data

if os.path.exists(full_path_to_file):
    with open(full_path_to_file, "r") as ninja_file:
        contents = ninja_file.read()

# Output message from file
print(contents)

score_data = \
    """
    The latest game info right on your board !!
    Player Name: {}
    Attempts to Win: {}
    """.format(player, attempts)

# Output message from code
print(score_data)

##############################################################################################
