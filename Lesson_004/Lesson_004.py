# List and dictionaries

"""
Resources:
https://www.w3schools.com/python/python_lists.asp
"""

##############################################################################################
new_list = []  # defining an empty list
some_list = [1, 34, 12, 17, 87]
another_list = ["tesla", "toyota", "nissan"]
mixed_list = [22, "elon", True, "SmartNinja", 3.14, None]

"""
Note: List are mutable data structures
"""

# List anatomy
# Indexing:
# print(mixed_list[1])  # Should print "elon"
# print(mixed_list[-2])  # Should print "SmartNinja"
#
list_element = mixed_list[0]
# print(list_element)

# slicing
new_list = mixed_list[1:-1]  # slicing = [start:stop]
# print(new_list)

##############
# List Methods

# append
my_var = "house"
mixed_list.append(my_var)  # Adds an element at the end of the list
# print(mixed_list)

# insert
my_other_var = "inserted_at_index_0"
my_other_var = "inserted_at_index_2"
mixed_list.insert(0, my_other_var)
mixed_list.insert(2, my_other_var)
# print(mixed_list)

# pop
popped_element = mixed_list.pop(-1)
# print(popped_element)

# remove
mixed_list.remove("elon")
# print(mixed_list)

# reverse
mixed_list.reverse()
# print(mixed_list)

# index
index_of = mixed_list.index("SmartNinja")
# print(index_of)

# Note
"""
List are called iterable objects because them support iteration
G.E: 
for element in some_list:
    print(element)
"""

##############
# Dictionaries
box = {"height": 20, "width": 45, "length": 30}

# Get the box width
# print(box["width"])

# Get the box length
# print(box["length"])

# Dictionary methods
dict_keys = box.keys()
# print(dict_keys)

dict_values = box.values()
# print(dict_values)

dict_items = box.items()
# print(dict_items)

# Iterating over a dictionary with .items()
for key, value in box.items():
    pass
    # print(key, value)

# creating a dictionary dynamically
mixed_list = [22, "elon", True, "SmartNinja", 3.14, None, [1, 2, 3, 4, [1, 2]], {}]
new_dict = {}

for index, element in enumerate(mixed_list):
    new_dict[str(index)] = element

for key, val in new_dict.items():
    pass
    # print(key, val)

# nested dict
movies = {"categories": {"accion": {"pg18": ["predator", "terminator"], "pg13": ["avengers", "thor"]}, "terror": {}}}

for key, val in movies.items():
    # unpack the first level of the nested structure
    # print(key, val)
    pass

# Sets python
# With sets we can filter data deleting the repeated elements of a list
my_list = [1, 2, 3, 3, 3, 3, 5, 6, 8, 5, 10]
print(set(my_list))
print(list(set(my_list)))

##############################################################################################
