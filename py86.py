# Iterables in Python
# An iterable is an object or collection that can return its elements one at a time.
# This allows it to be iterated over (looped through) using constructs like for loops.
# Common iterables include lists, tuples, sets, strings, and dictionaries.

# Example of a list (ordered, mutable, allows duplicates)
my_list = [1, 2, 3, 4, 5]

# Iterating over a list with a for loop
# The loop variable (e.g., 'item' or 'number') is a temporary name for the current element.
# Choose descriptive names for readability.
for item in my_list:
    print(item)

# You can use reversed() to iterate backwards (works for lists, tuples, strings, but not sets)
for number in reversed(my_list):
    print(number)

# Customizing print output with the 'end' parameter
# By default, print() ends with a newline (\n). You can change it to space, dash, etc.
for number in my_list:
    print(number, end=" ")  # Outputs on one line separated by spaces

print()  # Newline for separation

for number in my_list:
    print(number, end="-")  # Outputs with dashes

print()  # Newline

# Tuple example (ordered, immutable, allows duplicates)
my_tuple = (1, 2, 3, 4, 5)

for number in my_tuple:
    print(number)

# Set example (unordered, mutable, no duplicates, no guaranteed order)
my_set = {"apple", "orange", "banana", "coconut"}

for fruit in my_set:
    print(fruit)

# Note: Sets are not reversible. reversed(my_set) raises TypeError: 'set' object is not reversible

# String example (sequence of characters, immutable)
my_name = "Bro Code"

for character in my_name:
    print(character, end=" ")  # Print characters separated by space

print()

# Dictionary example (key-value pairs, unordered in older Python, insertion order preserved since 3.7+)
my_dictionary = {'A': 1, 'B': 2, 'C': 3}

# Iterating over dictionary by default gives keys
for key in my_dictionary:
    print(key)

# To iterate over values only, use .values()
for value in my_dictionary.values():
    print(value)

# To iterate over both keys and values, use .items()
# This unpacks each key-value pair into two variables
for key, value in my_dictionary.items():
    print(f"{key} = {value}")

# Alternative formatting
for key, value in my_dictionary.items():
    print(key, "=", value)

# Summary:
# - Anything you can use in a 'for item in iterable:' loop is an iterable.
# - Lists, tuples, sets, strings, dictionaries, range objects, etc., are iterables.
# - Iteration works by calling iter() under the hood to get an iterator, then next() repeatedly.
# - The for loop handles StopIteration automatically.
# - Good practice: Use meaningful loop variable names for code clarity.