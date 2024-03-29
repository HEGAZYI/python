"""
1-Write a function that accepts two arguments (length, start) to generate an array of a specific
length filled with integer numbers increased by one from start
"""
def generate(length, start):
    arr = []
    for i in range(length):
        arr.append(start + i)
    return arr

result = generate(5, 10)
print(f"the array elements : {result}")

print("--------------------------------")

"""
2-Fill an array of 5 elements from the user, sort it in descending and ascending orders then
display the output.
"""
arr = []
for i in range(5):
    user_input = int(input(f"enter element #{i+1} of the array :"))
    arr.append(user_input)
descending_order = sorted(arr, reverse=True)
ascending_order = sorted(arr)
print("Original array:", arr)
print("Descending order of the array:", descending_order)
print("Ascending order of the array:", ascending_order)

print("--------------------------------")

"""
3-Write a function which has an input of a string from user then it will return the same string
reversed.
"""
def reverse(my_string):
    reversed_string = my_string[::-1]
    return reversed_string

input_string = input("enter a string val: ")
result = reverse(input_string)
print(f"the reversed string: {result}")

print("--------------------------------")

"""
4. Write a Python program to length & sum all the items in a list.
5. Write a Python program to get the largest & smallest number from a list.
"""
my_list = [2, 5, 7, 4, 8, 12, 13, 10]
print(f"the length of the list: {len(my_list)}")
print(f"the sum of the list items: {sum(my_list)}")
print(f"the maximum value of the list items: {max(my_list)}")
print(f"the minimum value of the list items: {min(my_list)}")

print("--------------------------------")

"""
6. Write a Python program to select the odd & even items from a list.
"""
new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
odd_items = []
even_items = []
for i in range(len(new_list)):
    if new_list[i] % 2 == 0:
        even_items.append(new_list[i])
    else:
        odd_items.append(new_list[i])
print(f"odd items of the list in ascending order:{sorted(odd_items)}")
print(f"even items of the list in ascending order:{sorted(even_items)}")

print("--------------------------------")

"""
7. Write a Python program to find common items in two lists.
"""
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_items = list(
    set(list1) & set(list2))  # using sets to find intersections(&),unions(|)
print("Common items by the way of sets :", common_items)
# another way without useing sets
common_items = [i for i in list1 if i in list2]
print("Common items by using the way of generating lists:", common_items)

print("--------------------------------")

"""
8-Create a dictionary from a list of strings where the first char of the string act as key and
respective strings are stored as values. Take input from user
"""
def create_dictionary(strings):
    dict1 = {}
    for string in strings:
        key = string[0]
        if key in dict1:
            dict1[key].append(string)
        else:
            dict1[key] = [string]
    return dict1

# Example usage:
input_strings = input("Enter a list of strings separated by spaces: ").split()
dict = create_dictionary(input_strings)
print(dict)

print("--------------------------------")
"""
9-Below are two lists. Write a Python program to convert them into a dictionary in a way that
item from list 1 is the key and item from list2 is the value.
"""
Keys = ["ten", "twenty", "thirty"]
Values = [10, 20, 30]
dict = {Keys[i]: Values[i] for i in range(len(Keys))}
print(dict)

print("--------------------------------")
"""
10. Take input from user and find words with both alphabets and numbers.
"""
user_input = input("Enter your phrase: ").split()
store_output = []
for string in user_input:
    has_alphabet = False
    has_number = False
    for char in string:
        if char.isalpha():
            has_alphabet = True
        elif char.isdigit():
            has_number = True
    if has_alphabet and has_number:
        store_output.append(string)
print(store_output)

print("--------------------------------")


"""
Bonus: Write a python Program to print all Possible Combinations from the three Digits
Input: [1, 2, 3]
"""
Input = [1, 2, 3]
for I1 in Input:
    for I2 in Input:
        for I3 in Input:
            if I1 != I2 and I1 != I3 and I2 != I3:
                print(I1, I2, I3)
print("--------------------------------")
