# get type of any entered phrase
get_type = print(type(3))
get_type = print(type(3.5))
get_type = print(type("3"))
get_type = print(type(True))

print("--------------------------------------")

# casting
A = int(1)
B = int(3.4)
C = float(3)
D = str(4)
print(A)
print(B)
print(C)
print(D)

print("--------------------------------------")

# basic string
string1 = "hello 'world'"
string2 = 'hello "world"'
string3 = "hello 'world'"
print(string1)
print(string2)
print(string3)

print("--------------------------------------")

new_line = "name :alice.\nage :22"
print(new_line)
tabbed_text = "name :\talice.\nage :\t22"
print(tabbed_text)

print("--------------------------------------")

# concatination
concat_string = "hello"
concat_string += " world"
print(concat_string)

print("--------------------------------------")

# formatted string
x = "welcome"
y = "to python course"
print(f"{x} {y}")  # ==> x + " " + y

print("--------------------------------------")

# repeated string
repeated_string = "python " * 3
print(repeated_string)  # python prthon python

print("--------------------------------------")

# indexing
phrase = "dreams always become truth"
print(phrase[0])  # index 0 ==> first letter
print(phrase[6])  # index 6 ==> last letter of dreams
print(phrase[0:6])  # from the first letter to the last letter of the first word
print(phrase[1:5])  # from the second letter before the 's' letter of the first word
print(phrase[-1])  # the last index ==> h
print(phrase[::2])  # take index 0 2 4 6 8 10 ,and so
print(phrase[::1])  # the total phrase
print(phrase[::-1])  # reverse the phrase
print(phrase[:])  # print all phrase

print("--------------------------------------")


# palindrome
string = "lili"
if string == string[::-1]:
    print("palindrome")
else:
    print("not palindrome")

print(string)

print("--------------------------------------")

# string functions
mystr = " hello , alice "
print(mystr.upper())  # convert the string to uppercase
print(mystr.lower())  # convert the string to lowercase
print(mystr.title())  # make your string like title case
print(mystr.split(","))  # splits your dtring into a substring
print(mystr.strip())  # removes any white spaces at the beginning or the end

print("--------------------------------------")

# string is immutable ==> can not change any index in the string
"""str = "ali"
str[0] = "s"
print(str)"""

# you can use replace("old_letter","new_letter") to replace any letter
new_string = "alice"
new_string = new_string.replace("a", "A")
print(new_string)

new_string1 = "hello , alice"
new_string1 = new_string1.replace("o", "O", 2)  # convert two letters 'o' to 'O'
print(new_string1)

print("--------------------------------------")
# string formatting
name = "Alice"
print("my name is "+str(name))
print(f"my name is {name}")
print("my name is %s" %name)

age = 22
print("my age : " + str(age))
print(f"my age : {age}")
print("my age : %s" % age)

print("--------------------------------------")
# input()
user_input = input("enter your name:")
print(f"hello {user_input}")

print("--------------------------------------")
