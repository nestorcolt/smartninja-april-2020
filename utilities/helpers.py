import json
import os

##############################################################################################
# Globals
current_directory = os.getcwd()
parent_directory = os.path.split(current_directory)[0]
file_name = "game_score.json"
full_path_to_file = os.path.join(parent_directory, "data", file_name)


##############################################################################################

def save_score(stored_score):
    with open(full_path_to_file, "w") as ninja_file_2:
        ninja_file_2.write(json.dumps(stored_score,
                                      indent=4,
                                      separators=[",", ":"]))


def load_score():
    # Read store score at start of the game
    with open(full_path_to_file, "r") as ninja_file_2:
        try:
            stored_score = json.load(ninja_file_2)
        except Exception as e:
            stored_score = None

        return stored_score
