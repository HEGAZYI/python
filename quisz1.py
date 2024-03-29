""" A.H.M"""

#: Use a for loop to print the numbers from 1 to 20,inclusive.
for i in range(20):
    print(i + 1)

print("----------------------------------")

# Make a list of the numbers from one to one million, and then use a for loop to print the numbers
numbers = list(range(1, 1000001))
for i in numbers:
    print(i)

print("----------------------------------")

# Make a list of the numbers from one to one million, and
# then use min() and max() to make sure your list actually starts at one and ends
# at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
numbers = list(range(1, 1000001))
print("Minimum number in the list:", min(numbers))
print("Maximum number in the list:", max(numbers))
sum_of_numbers = sum(numbers)
print("Sum of the numbers in the list:", sum_of_numbers)

print("----------------------------------")

#: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.
odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)

print("----------------------------------")

#: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
multiples = list(range(3, 31, 3))
for number in multiples:
    print(number)

print("----------------------------------")

#: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
cube = list(range(1, 11))
for i in cube:
    print(i**3)

# the same output like a list
cube = [i**3 for i in range(1, 11)]
print(cube)

print("----------------------------------")
