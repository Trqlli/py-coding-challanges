# Beginner:

# 1:
# Make two functions:
# 1. A function that checks if a list has more than 6 items. Returns bool (Boolean)
# 2. A function that uses the first function and prints if the given list has more or less than 6 items.

# The lists:
# [31, 123, 420, 69, 34, 89, 105]
# [90, 2123, 3435]

# Hint: Boolean = True or False

# 2:

# Make a function that counts to a given number

# Hint: for loop


# Intermediate:

# 1:
# Make a while loop inside a function that prints the time (H, M, S) every second

# Hint: When a while function is set to true it executes until its interrupted
# Use a function from the time module to make the cooldown (you need to import it)
# Try using the string-formatted time function

# 2:
# Make a function that checks how many peoples name from a list starts with the letter A

# Names:
# ["Alex", "Linkx", "Trolli", "Alec"]

# Hint: .startswith()

# Hard:

# 1:
# Make a function that requires the parameters name and age. Make two input fields that ask the name and age.
# There cannot be numbers in the name and there cannot be letters in the age.

# Hint: You will need any() and map() combined for checking the str. You can also use a for loop
# You can use .isalpha to check if a str has numbers and .isdigit to check if a string has digits in it

# any(): Checks if something in a str, list... is an iterable(if something in the list == true)
# map(): Makes function apply to each item in str, list... if item is iterable






































# Easy Solution
# 1:
def check_list_bool_exercise(list) -> bool:
    if len(list) < 6:
        return True
    else:
        return False


def list_check(list):
    if check_list_bool_exercise(list):
        print("The list is under the limit")
    else:
        print("The list is over the limit")


list_check([31, 123, 420, 69, 34, 89, 105])
list_check([90, 2123, 3435])


# 2:
def count(number):
    for i in range(number):
        i += 1
        print(i)


# Intermediate Solution
# 1:
import time


def print_time_loop():
    while True:
        print(time.strftime("%H:%M:%S"))
        time.sleep(1)


print_time_loop()


# 2:
def check_name_start_letter(names):
    count = 0
    for i in names:

        if i.startswith("A"):
            count += 1
    print(f"{count} people's names start with A")


# Hard Solution
def name_age_check():
    name = input("What is your name? ")

    if any(map(str.isdigit, name)):
        print("You can't have numbers in your name!")
    else:
        age = input("What is your age? ")
        if any(map(str.isalpha, age)):
            print("You can't have letters in your age!")
        else:
            print(f"Your name is {name.title()} and you are {age} years old")


name_age_check()


# With for loop
def name_age_check():
    name = input("What is your name? ")

    if any(i.isdigit() for i in name):
        print("You can't have numbers in your name!")
    else:
        age = input("What is your age? ")
        if any(j.isalpha() for j in age):
            print("You can't have letters in your age!")
        else:
            print(f"Your name is {name.title()} and you are {age} years old")


name_age_check()
