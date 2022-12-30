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
    count = 0
    while count <= number:
        print(count)
        count += 1

count(10)

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
