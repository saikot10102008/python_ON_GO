"""
PYTHON `in` KEYWORD - BEGINNER FRIENDLY NOTES

This file explains the `in` keyword in Python using simple comments and examples.

What `in` means:
- It checks whether a value exists inside something.
- It is also used in `for` loops to read items one by one.

We will keep this simple and avoid OOP, file handling, and advanced Python topics.
"""


# =========================================================
# 1. WHAT IS THE `in` KEYWORD?
# =========================================================
# The `in` keyword is used to ask a question:
# "Is this value inside that collection or text?"
#
# It usually gives a True or False answer.


print("1) `in` keyword with a string")
text = "python is fun"

# Check whether a smaller text exists inside a bigger text
print("'python' in text ->", "python" in text)   # True
print("'fun' in text    ->", "fun" in text)      # True
print("'java' in text   ->", "java" in text)     # False
print("-")


# =========================================================
# 2. `in` WITH LISTS
# =========================================================
# A list stores many items inside square brackets [ ]
# `in` checks whether an item is present in that list.

print("2) `in` keyword with a list")
fruits = ["apple", "banana", "mango", "orange"]

print("'banana' in fruits ->", "banana" in fruits)  # True
print("'grape' in fruits  ->", "grape" in fruits)   # False
print("-")


# =========================================================
# 3. `in` WITH TUPLES
# =========================================================
# A tuple stores many items inside round brackets ( )
# Tuples are similar to lists, but their values are usually not changed.

print("3) `in` keyword with a tuple")
numbers = (10, 20, 30, 40)

print("20 in numbers ->", 20 in numbers)   # True
print("50 in numbers ->", 50 in numbers)   # False
print("-")


# =========================================================
# 4. `in` WITH SETS
# =========================================================
# A set stores unique items inside curly braces { }
# `in` works here too.

print("4) `in` keyword with a set")
colors = {"red", "green", "blue"}

print("'green' in colors ->", "green" in colors)  # True
print("'yellow' in colors ->", "yellow" in colors)  # False
print("-")


# =========================================================
# 5. `in` WITH DICTIONARIES
# =========================================================
# A dictionary stores key-value pairs.
# When you use `in` with a dictionary, Python checks KEYS only.

print("5) `in` keyword with a dictionary")
student = {
	"name": "Aman",
	"age": 20,
	"city": "Delhi"
}

# These checks look for keys, not values
print("'name' in student ->", "name" in student)   # True
print("'age' in student  ->", "age" in student)    # True
print("'Aman' in student ->", "Aman" in student)   # False, because 'Aman' is a value
print("-")


# =========================================================
# 6. `not in` KEYWORD
# =========================================================
# `not in` is the opposite of `in`
# It checks whether something is NOT present.

print("6) `not in` keyword")

print("'grape' not in fruits ->", "grape" not in fruits)   # True
print("'apple' not in fruits ->", "apple" not in fruits)   # False
print("-")


# =========================================================
# 7. `in` IN A `for` LOOP
# =========================================================
# Another very common use of `in` is in a `for` loop.
# It means: take each item from the collection one by one.

print("7) `in` keyword in a for loop")

for fruit in fruits:
	# The variable 'fruit' gets one item at a time from the list
	print("Fruit:", fruit)

print("-")


# =========================================================
# 8. HOW `in` WORKS IN SIMPLE WORDS
# =========================================================
# Think of `in` like asking:
# - Is this word inside this sentence?
# - Is this item inside this list?
# - Is this key inside this dictionary?
#
# It helps us search in a very easy way.

sentence = "I love learning Python"

print("8) Simple search examples")
print("'love' in sentence ->", "love" in sentence)   # True
print("'Java' in sentence ->", "Java" in sentence)   # False
print("-")


# =========================================================
# 9. USING `in` IN A REAL-LIFE STYLE CHECK
# =========================================================
# Imagine we want to check whether a name is in a small list.

names = ["Ravi", "Sita", "Mohan", "Neha"]
search_name = "Neha"

print("9) Real-life style check")
if search_name in names:
	print(search_name, "is present in the list")
else:
	print(search_name, "is not present in the list")
print("-")


# =========================================================
# 10. IMPORTANT THINGS TO REMEMBER
# =========================================================
# 1. `in` usually returns True or False.
# 2. It works with strings, lists, tuples, sets, and dictionaries.
# 3. With dictionaries, it checks keys.
# 4. `not in` is the opposite of `in`.
# 5. `in` is also used in `for` loops.

print("10) Summary")
print("`in` checks if something exists inside a collection or string")
print("`not in` checks if something does not exist")
print("`for item in collection` reads items one by one")


# =========================================================
# 11. SMALL PRACTICE SECTION
# =========================================================
# Try to predict the answers before running the code.

animals = ["cat", "dog", "rabbit"]

print("11) Practice")
print("'cat' in animals   ->", "cat" in animals)    # True
print("'lion' in animals  ->", "lion" in animals)   # False
print("'lion' not in animals ->", "lion" not in animals)  # True


print("\nEnd of `in` keyword notes")
