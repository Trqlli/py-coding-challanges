
# Make a variable
your_variable = str or int

# Add to an int
your_int = 0
your_int += 1  # Added 1

# Make a list/array
your_list = [1, "2", 3, "4"]

# Make a dictionary
your_dictionary = {"item": "value"}

# Get item from dictionary
print(your_dictionary["item"])
print("{item}".format(**your_dictionary))


# Make a tuple
your_tuple = ("item1", "item2", "item3")

# Get user input
user_input = input()


# Make a function
def your_function():
    # Your code...
    pass

# Anonymous function (rarely used)
anonymous_function = lambda a: a*5
print(anonymous_function(a=5))  # Result 25

# Reverse a string
your_string = "Hello World"
reversed_string = your_string[::-1]

# or
reverse = "".join(list(reversed("Reverse")))


# Check if a string startswith something
name = "Max"
if name.startswith("M"):
    # Your code
    pass

# Make a for loop
for i in range(1):
    # Your code...
    pass

# Make a while loop
while True:
    # Your code...
    pass
