# Variables
##############################################################################################
link_to_video = r"https://www.loom.com/share/21b1000ad71b40bea7f086a9aab4a510"
github = "https://github.com/nestorcolt/smartninja-april-2020"

x = 10
y = 7

result = x + y
# print(result)

# Variables more than numbers !
some_string = "Hey there!"
# print(some_string)

string_a = "Hello"
string_b = "World!"

# print(string_a + string_b)
# print(string_a + " " + string_b)

# Booleans
bool_one = True
bool_two = False
# print(bool_two)

# None
some_var = None
# print(some_var)

# User inputs
# user_name = input("Please enter your name: ")
# print("Hello " + user_name + "!")

# Flow control (if/elif/else)
# Mood checker
mood = "scared"

if mood == "happy":
    print("It is great to see you happy!")

elif mood == "nervous":
    print("Take a deep breath 3 times.")

elif mood == "scared":
    print("Take a deep breath 10 times.")

else:
    print("Cheer up, mate!")

##############################################################################################
# Q&A
mood = "sad"

if mood == "happy":
    print("input: happy")

elif mood == "sad":
    print("input: sad")

elif mood == "angry":
    print("input: sad")

elif mood == "tears":
    print("input: sad")

else:
    print("ELSE CONDITION!")
