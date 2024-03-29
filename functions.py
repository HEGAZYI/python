"""
functions:
1. Defining a Function.
2. Passing Arguments.
3. Return Values.
4. Passing a List
5. Passing an Arbitrary Number of Arguments
"""

# 1. Defining a Function.
"""• The first line uses the keyword def to inform Python that you’re defining a function."""


def get_user(user):
    print(f"Hello!,{user}")


user = input("enter you name:")
get_user(user)

print("--------------------------------------")

# 2. Passing Arguments
"""
You can pass arguments to your functions in a number of ways.
You can use positional arguments, which need to be in the same order the parameters were
written; keyword arguments, where each argument consists of a variable name and a value; and
lists and dictionaries of values.
"""
# A. Positional Arguments
"""
• Python must match each argument in the function call with a parameter in the function definition.
• The simplest way to do this is based on the order of the arguments provided.
• Values matched up this way are called positional arguments
"""


def animal(animal_type, animal_name):
    print(f"i have {animal_type}")
    print(f"my {animal_type}'s name is {animal_name.title()}")


animal("hamster", "harry")

# B. Keyword Arguments
"""
• A keyword argument is a name-value pair that you pass to a function.
• You directly associate the name and the value within the argument.
• Keyword arguments free you from having to worry about correctly ordering your arguments in the
function call, and they clarify the role of each value in the function call. 
"""


def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="harry", animal_type="hamster")  # don not care about order

# C. Default Values
"""
• When writing a function, you can define a default value for each parameter.
• If an argument for a parameter is provided in the function call, Python uses the argument value. If
not, it uses the parameter’s default value.
• So when you define a default value for a parameter, you can exclude the corresponding
argument you’d usually write in the function call.
• Using default values can simplify your function calls and clarify the ways your functions are used.
"""


def describe_pet(pet_name, animal_type="dog"):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name="willie")
describe_pet(pet_name="harry", animal_type="hamster")

# D. Equivalent Function Calls
""" A dog named Willie."""
describe_pet("willie")
describe_pet(pet_name="willie")
""" A hamster named Harry."""
describe_pet("harry", "hamster")
describe_pet(pet_name="harry", animal_type="hamster")
describe_pet(animal_type="hamster", pet_name="harry")

print("--------------------------------------")

# 3. Return Values
"""A.Returning a Simple Value"""


def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)  # expected output Jimi Hendrix

"""B. Returning a Dictionary"""


def build_person(first_name, last_name):
    person = {"first": first_name, "last": last_name}
    return person


musician = build_person("jimi", "hendrix")
print(musician)

"""c. Using a Function with a while Loop"""


def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


f_name = input("First name: ")
l_name = input("Last name: ")
formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}!")

print("--------------------------------------")

# 4. Passing a List
"""A. Using a Function with a while Loop"""


def greet_users(names):
    for n in names:
        msg = f"hello , {n}"
        print(msg.title())


names = ["harry", "alian", "rose"]
greet_users(names)

"""B. Modifying a List in a Function """


def remove_odds(numbers):
    for i in range(len(numbers) - 1, -1, -1):  # loop backword to safe removal
        if numbers[i] % 2 != 0:
            numbers.remove(numbers[i])


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"the original list:{numbers}")
remove_odds(numbers)
print(f"the new list without odd numbers:{numbers}")

"""
C. Preventing a Function from Modifying a List
• Sometimes you’ll want to prevent a function from modifying a list.
• In this case, you can address this issue by passing the function a copy of the list, not the original.
• Any changes the function makes to the list will affect only the copy, leaving the original list intact. 
"""


def modify_list(lst):
    # This function modifies the list
    lst.append(100)


original_list = [1, 2, 3, 4, 5]
print("Original list:", original_list)
# Pass a copy of the list to the function
modified_list = original_list.copy()
modify_list(modified_list)
print("Modified list:", modified_list)
print("Original list (unchanged):", original_list)

print("--------------------------------------")

# 5. Passing an Arbitrary Number of Arguments
"""
A. Mixing Positional and Arbitrary Arguments
• If you want a function to accept several different kinds of arguments, the parameter that
accepts an arbitrary number of arguments must be placed last in the function definition.
• Python matches positional and keyword arguments first and then collects any remaining arguments
in the final parameter.
• For example, if the function needs to take in a size for the pizza, that parameter must come before
the parameter *toppings
"""


def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")


"""
B. Using Arbitrary Keyword Arguments
• Sometimes you’ll want to accept an arbitrary number of arguments, but you won’t know ahead of
time what kind of information will be passed to the function.
• In this case, you can write functions that accept as many key-value pairs as the calling statement
provides.
• One example involves building user profiles: you know you’ll get information about a user, but
you’re not sure what kind of information you’ll receive. 
"""
def build_user_profile(username, **user_info):
    # Create a dictionary to store the user's profile
    profile = {"username": username}

    # Add any additional user information provided
    for key, value in user_info.items():
        profile[key] = value

    return profile

# Example usage:
user1_profile = build_user_profile("john_doe", first_name="John", last_name="Doe", age=30)
print(user1_profile)
user2_profile = build_user_profile("jane_smith",first_name="Jane",last_name="Smith",location="New York",occupation="Engineer",)
print(user2_profile)

print("--------------------------------------")
