from Lesson_005 import module_005

"""
Importing a function into a module
"""

# Using function from module_005
module_005.greeting_message(username="Mireia")
message = module_005.say_hello_with_return(name="Nestor")

# Yes
print(message)

# Uhmmm not that much
print(module_005.say_hello_with_return(name="Nestor"))

##############################################################################################
