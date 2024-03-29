"""A.H.M """
"""
# Slicing
my_list = [1, 2, 3, 4, "A", "B", "C", 5, 6, 7, 8]
slice1 = my_list[0:4]
print(f"the first four elements in the list :\n{slice1}")
slice2 = my_list[4:7]
print(f"the middle three elements in the list :\n{slice2}")
slice3 = my_list[7:11]
print(f"the last four elements in the list :\n{slice3}")

# Pizza
my_pizza = ["Margherita", "Pepperoni", "Hawaiian", "Meat", "Lover's", "Veggie Supreme"]
friend_pizza = ["Cheese", "Mushroom", "Olive", "Buffalo", "Chicken", "Spinach"]
print("my favorite pizzas are:")
for i in my_pizza:
    print(i)
print("my friend favorite pizzas are:")
for i in friend_pizza:
    print(i)
"""

# Pizza
my_pizza = ["Margherita", "Pepperoni", "Hawaiian"]
counter=0
for pizza  in my_pizza:
    counter=counter+1
    print(f"{counter}-{pizza}")

print("============================================")

for p in my_pizza:
    print(f"i like \" {p} \" pizza")

print("============================================")

print("""I absolutely adore pizza; its cheesy goodness and flavorful toppings are irresistible to me.
Whenever I crave comfort food, a slice of pizza never fails to satisfy my taste buds.
Pizza is my go-to choice for a delicious and satisfying meal,whether I am dining out with friends or enjoying a cozy night in.""")

print("============================================")
# animals
my_animals = ["dog","cat","birds"]
counter = 0
for animal in my_animals:
    counter = counter + 1
    print(f"{counter}-{animal}")

print("============================================")

print(f"\" {my_animals[0]} \"would make a great pet  ")
print(f"\" {my_animals[1]} \"is very cure  ")
print(f"\" {my_animals[2]} \"have a beatifull sound  ")

print("============================================")
print("i love animals")
