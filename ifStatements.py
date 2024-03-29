"""
if statements are used for checking 
"""
print("--------------------------------------")
car = "Audi" #assign value to variable car as a string
check = (car.lower() == "audi") #check for the value in the car variable 
print(check)

# check on element in a list
cars = ["audi","bmw","toyota","bugatti"]
list_check = "bmw" in cars #check for bmw in cars
print(list_check)
# using for loop
car = "bmw"
for car in cars:
    print("True")

print("--------------------------------------")
# using if-else statements
name = input("enter your name:")
age = int(input("enter your age:"))
if age > 16:
    print(f"hello {name},you are old enough to our journey")
else:
    print(f"sorry {name},you are too young")

print("--------------------------------------")
# using if-elif-else chain
age = int(input("enter your age:"))
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 60:
    price = 40
else:
    price = 20
print(f"Your admission cost is {price}")

print("--------------------------------------")
# using if with lists
requested_toppings = ["mashrooms", "green peppers", "extra cheese"]
for topping in requested_toppings:
    if(topping == "green peppers"):
        print("sorry , we are out of green peppers right now.")
    else:
        print(f"adding {topping}.")

print("out pizza is finshed...")  

print("--------------------------------------")
