import random

# RESOURCES
# Relational operator
# https://data-flair.training/blogs/python-comparison-operators/
##############################################################################################
# Guess the secret number INIT

# WHILE LOOP
secret = 22
guess = 0

# while guess != secret:
while False:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You guessed it - congratulations! It's number 22.")
        break
    else:
        print("Sorry, your guess is not correct... The secret number is not " + str(guess))

##############################################################################################
# FOR LOOP

secret = 22

for index in range(5):
    continue  # This continue is to avoid the rest of the logic execution
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if index == 2:
        print("skipping number {}".format(index))
        continue  # continue bypass and skips the rest of the for loop if a condition match

    if guess == secret:
        print("You've guessed it - congratulations! It's number 22.")
        break  # metodo de escape del loop al cumplirse la condicion
    else:
        print("Sorry, your guess is not correct... The secret number is not " + str(guess))

    print("Current Index: {}".format(index))

##############################################################################################

# Guess the secret number (if/elif)


# secret = random.randint(1, 30)
secret = 22

while False:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number 22.")
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

##############################################################################################
# HOMEWORK - STRINGS
# https://www.w3schools.com/python/python_ref_string.asp
# String is a non-mutable object

a_string = "this is a string in python 3"
"""

print(a_string.capitalize())
print(a_string.title())
print(a_string.upper())
print(a_string.lower())

"""

# Iterate over string with a for loop
"""
for char in a_string:
    # Create condition to check IF CHARACTER IS DIGIT
    if char.isdigit():
        print(char)

"""

a_string = "this is a string in python 3"

# replace
# print(a_string)
# b_string = a_string.replace("this", "that")
# print(b_string)

# split
# print(a_string)
# result_list = a_string.split(" ")
# print(result_list)

# index
# print(a_string.index("t"))
# # print(a_string.index("i"))
# # print(a_string.index("3"))

# string format in python
lenguage = "Python"
python_version = 3.8
username = "NestorColt"
user_warning_message_template = "Attention user: {2}, this is a test of string formatting in {0} version: {1}"

print(user_warning_message_template.format(username, lenguage, python_version))

"Attention user: NestorColt, this is a test of string formatting in Python version: 3.8"
"Attention user: 3.8, this is a test of string formatting in NestorColt version: Python"

