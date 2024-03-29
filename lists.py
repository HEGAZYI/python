# lists
a = [1, 2, 3]
print(a)
a.append(4)
a.append(5)
print(a)

# replacing elements of list
a[3] = "G"
print(a)
a.append("welcome")
print(a)

print("--------------------------------------")

# a[5][0] = "W"  ==> here you replace a character in the string ,and this is not allwed

# get the length of the list
print(f"the length of the list is : {len(a)}")

print("--------------------------------------")

# get the type of the list
b = [1, 2, 3, 4]
print(f"the type of the b is : {type(b)}")

print("--------------------------------------")

# using the list() constructor
thislist = list(("a", "b", "c"))
print(thislist)

print("--------------------------------------")

# using join method to make the list like string
c = ["welcome", " to", " python"]
result = " ".join(c)
print(result)

print("--------------------------------------")

# extending or joining two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

print("--------------------------------------")

# looping the list
x = [1, 2, 3]
for i in x:
    print(i)

print("--------------------------------------")

# range object
print(list(range(0, 6)))

print("--------------------------------------")

# using range to print list
Y = [1, 2, 3, 4, 5, 6, 7]
l = len(Y)
for i in range(l):
    print(Y[i])  # print elements of list
print("\n")
for i in range(l):
    print(i)  # print indexes of list

print("--------------------------------------")

# search in list
Z = [1, 2, 3, 4, "ahmed"]
if "ahmed" in Z:
    print("found")

print("--------------------------------------")

# min,max,sum
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(my_list))
print(max(my_list))
print(sum(my_list))

print("--------------------------------------")

# adding new elements
family = ["liza",1.74,"emma",1.68,"mom",1.71,"dad",1.75]
print(family)
family[0:2]=["shon",1.8]
print(family)
family = family + ["me",1.8]
print(family)


print("--------------------------------------")

# List Methods and Functions
list1 = [1,2,3,4,5,6,7]
print(len(list1)) #print the length of the list
print(list1.count)  # Return number of occurrences of value
list1.append(22)#add a new element at end
print(list1)
print("--------------------------------------")

migicians = ["alice","darwin","anglo"]
for migician in migicians:
    print(f"{migician.title()}, that was a great trick")
    print(f"i can't wait for your next trick ,{migician.title()}")
print("thank everyone")    

print("--------------------------------------")

# get even numbers
even_number = list(range(2,11,2))
print(even_number)

# get odd numbers
odd_number = list(range(1,12,2))
print(odd_number)

print("--------------------------------------")

"""
List comprehension
•A list comprehension allows you to generate this
same list in just one line of code.
•A list comprehension combines the for loop and the
creation of new elements into one line, and
automatically appends each new element.
"""
# ordinary code
squares = []
for value in range(1,11):
    value = value**2
    squares.append(value)
print(squares)    

# list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)

print("--------------------------------------")
# appending new elements at the end of the list
names = ["ahmed","ali","mohamed"]
print(names)
names.append("ashraf")
print(names)

# insert element at any index of the list
names.insert(0,"said")
print(names)
names.insert(2,"mahmoud")
print(names)

# Removing an Item Using the del Statement
del names[0] # you can't save the deleted element
print(names)

# Removing an Item Using the pop() Method
poped_element = names.pop() #you can  save the deleted element
print(poped_element)
first_poped = names.pop(0)  # you can  save the deleted element
print(first_poped)

# removing by value
removed_value = names.remove("mahmoud")
print(names)

print("--------------------------------------")
# sorting a list permanently
cars = ["bmw","audi","toyota","subaru"]
cars.sort()
print(cars)

# note that if the alphapitic is uppercase it will be the first sorted
cars = ["BMw", "audi", "Toyota","subaru", ]
cars.sort()
print(cars)

# Sorting a List Temporarily:can get the original list
cars = ["BMw","audi","Toyota","subaru",]
print("the original list:")
print(cars)
print("the sorted list:")
print(sorted(cars))
print("the original list again:")
print(cars)
