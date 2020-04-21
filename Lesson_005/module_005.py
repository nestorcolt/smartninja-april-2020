# Functions and reusability

def say_hello():
    print("Hello!")


##############################################################################################
# Without functions:

# Greeting message
# print("Hello my name is Nestor")

# with functions:

def greeting_message(username):
    print("Hello my name is {}".format(username))


""""

Functions helps the code to be easy to maintain and to scale helping usability
greeting_message(username="Nestor")
greeting_message(username="Felipe")
greeting_message(username="Mireia")
greeting_message(username="Mitzy")

"""


##############################################################################################
# Another function
def say_hello_with_return(name):
    return "Hello {0}!".format(name)
