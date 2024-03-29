"""
Tuples
•A tuple looks just like a list,
•you use parentheses instead of square brackets. [] => ()
•Python refers to values that cannot change
as immutable, and an immutable list is called
a tuple.
"""

dimensions = (100, 200, 300, 400, 500)
print(dimensions)
print(dimensions[0])  # first element in tuple
print(dimensions[::-1])  # reverse elements of tuple
# dimensions[0] = 235 # can not be done as tuple is immutable like strings

print("--------------------------------------")
# loop over tuples
tup = (10, 20, 30, 40, 50, 60, 70, 80, 90)
for t in tup:
    print(t)

print("--------------------------------------")
# writing over the tuple
a_tuple = (1, 2, 3, 4, 5)
print(a_tuple)
a_tuple = (6, 7, 8, 9, 0)
print(a_tuple)

print("--------------------------------------")
# you can remove parentheses
tup1 = ("mohamed", "ali")
tup2 = "mohamed", "ali"

print(tup1)
print(tup2)

print(type(tup1))
print(type(tup2))

print("--------------------------------------")
# tuple items is not unique
new_tuple = (1, 2.3, "ali", False)
print(new_tuple)
print(type(new_tuple[0]))
print(type(new_tuple[1]))
print(type(new_tuple[2]))
print(type(new_tuple[3]))

print("--------------------------------------")
# indexing
phrase = (1, 2, 3, 4, 5, 6, 7)
print(phrase[0])  # index 0 ==> first element
print(phrase[6])  # index 6 ==> last element of dreams
print(phrase[0:6])  # from the first element to the last element
print(phrase[1:5])  # from the second element before the element 6
print(phrase[-1])  # the last index ==> 7
print(phrase[::2])  # odd numbers
print(phrase[::-1])  # reverse tuple
print(phrase[:])  # show total tuple

print("--------------------------------------")
# tuple with one element
my_tuple = "david"
print(my_tuple)
print(type(my_tuple))  # string

my_tuple = ("david",)
print(my_tuple)
print(type(my_tuple))  # tuple wiyh one element

print("--------------------------------------")
# tuple concatination
a = (1, 2, 3, 4)
b = (5, 6, 7)
c = a + b
d = a + ("A", "B", "C") + b
print(c)
print(d)

print("--------------------------------------")
# tuple , list , string repeat (*)
tup = (1, 2)
string = "ahmed "
lis = [1, 2, 3]
print(tup * 6)
print(string * 6)
print(lis * 6)

print("--------------------------------------")
# methods
a = (1, 3, 7, 8, 2, 4, 5, 8)
print(f"the number of number 8 occurence : {a.count(8)}")
print(f"the index of number 2 : {a.index(2)}")

print("--------------------------------------")
# tuple destruct
a = ("A", "B", 4, "C")
x, y, _, z = a  # _ means ignore the third index
print(x)
print(y)
print(z)

print("--------------------------------------")
