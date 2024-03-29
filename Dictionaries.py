"""
Introduction to Dictionaries.
•A python dictionary is a collection of key and
value pairs.
•Keys must be unique in a dictionary, duplicate values
are allowed.
•Dictionary is a mutable data type in Python.
•Dictionary is wrapped in braces ({}) with a series of
key-value pairs.
•Example: alien_0 = {
‘color' : ‘green' , ‘points' : 5 }
"""

print("--------------------------------------")

# creating a dictionary
dict = {}
dict["color"] = "yellow"
dict["size"] = 22
print(dict)

print("--------------------------------------")
# keys + value
dictionary = {
    "first": "one",
    "second": "two",
    "third": "three",
}
print(dictionary.keys())
print(dictionary.values())
print("--------------------------------------")

# modifying dictionary
dic1 = {"color": "yellow", "size": 22}
print(f"the color of dic1 is {dic1['color']}")
dic1["color"] = "green"
print(f"now the color of dic1 is {dic1['color']}")

print("--------------------------------------")

# remove key-value pairs
dic2 = {"color": "yellow", "size": 22}
del dic2["size"]
print(dic2)

print("--------------------------------------")

# dictionary of similar objects
fav_language = {"jen": "python", "alian": "rust", "show": "c", "phil": "python"}
language = fav_language["alian"].title()
print(f"alian's favourite language is {language}")

print("--------------------------------------")

# using get() : if the key not exist you can handle the error using get() function
dic3 = {"color": "yellow", "size": 22}
print_value = dic3.get("point", "no point value assigned")
print(print_value)

print("--------------------------------------")

# Looping Through All Key-Value Pairs
fav_language = {"jen": "python", "alian": "rust", "show": "c", "phil": "python"}
for key, value in fav_language.items():
    print(f"\nkey:{key}")
    print(f"value:{value}")

    # looping for indexes without keys
    print("\nprinting the values without any key:")
for value in fav_language.values():
    print(value)

print("--------------------------------------")
"""
Nesting
• Store multiple dictionaries in a list, or a list of Items as a value in a dictionary. This is called nesting.
•You can nest dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside
another dictionary. Nesting is a powerful feature
We will go through:
1. A List of Dictionaries.
2. A List in a Dictionary
3. A Dictionary in a Dictionary
"""
# 1.a list of dictionary
user_0 = {"name": "ahmed", "age": 22}
user_1 = {"name": "mohamed", "age": 29}
user_3 = {"name": "ali", "age": 20}
users = [user_0, user_1, user_3]
for user in users:
    print(user)
print("--------------------------------------")
# 2.a list in dictionary
users = {"names": ["ahmed", "mohamed", "ali"], "ages": [22, 29, 20]}
print("our users have the following informations:")
for key, value in users.items():
    print(f"\n{key}:{value} ")
print("--------------------------------------")
# 3.a dictionary in dictionary
users = {
    "aeinstein": {"first": "albert", "last": "einstein", "location": "princeton"},
    "mcurie": {"first": "marie", "last": "curie", "location": "paris"},
}
for user_name, user_info in users.items():
    print(f"\nusername : {user_name}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location_info = f"{user_info['location']}"
    print(f"full name : {full_name.title()}")
    print(f"location : {location_info.title()}")
print("--------------------------------------")
# methods
# remove all informations in dictionary
dict = {"name": "ahmed", "age": 22, "length": 1.75}
print(dict)
dict.clear()
print(dict)

# update the dicionary
dict1 = {"name": "ahmed", "age": 22, "length": 1.75}
print(dict1)
dict1.update({"college": "FEE"})
print(dict1)

# make a copy of the dicionary
dict2 = {"name": "ahmed", "age": 22, "length": 1.75}
dict3 = dict2.copy()
dict2.update({"college": "FEE"})
print(dict2)
print(dict3)

# popitem: show the last element in the dictionary
dict4 = {"name": "ahmed", "age": 22, "length": 1.75}
print(dict4.popitem())

# items : print all items of the dictionary
dict5 = {"name": "ahmed", "age": 22, "length": 1.75}
allitems = dict5.items()
print(allitems)

# fromkeys(key,valu) : create a dictionary
a = ("first","second","third")
b = "a"
print(dict.fromkeys(a,b))
print("--------------------------------------")
