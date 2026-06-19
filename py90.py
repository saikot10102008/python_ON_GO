# Python Modules
# A module is a Python file (.py) containing functions, variables, and classes.
# Modules allow you to split your code into multiple files for better organization and reusability.

# --------------------
# 1. BASIC MODULE IMPORT
# --------------------
# Assume there is a file named 'my_module.py' in the same folder with:
# def greet(name):
#     return f"Hello, {name}!"
#
# def add(a, b):
#     return a + b
#
# pi = 3.14159

import my_module

# Accessing functions and variables using dot notation
print(my_module.greet("Bro"))
print("Sum:", my_module.add(5, 7))
print("Value of pi:", my_module.pi)

# --------------------
# 2. IMPORTING A SINGLE FUNCTION
# --------------------
# This is cleaner when you only need specific functions

from my_module import greet

print(greet("Alice"))

# Import multiple specific items at once
from my_module import greet, add

print("10 + 20 =", add(10, 20))

# --------------------
# 3. IMPORTING WITH ALIAS
# --------------------
# Useful for shortening long module names

import my_module as mm

print(mm.greet("Charlie"))

# Alias for a specific function
from my_module import add as addition
print("3 + 4 =", addition(3, 4))

# --------------------
# 4. STANDARD LIBRARY MODULES
# --------------------
# Python includes many built-in modules

import math
print("\n--- Math Module ---")
print("Square root of 16:", math.sqrt(16))
print("Pi constant:", math.pi)
print("Floor of 4.7:", math.floor(4.7))

import random
print("\n--- Random Module ---")
print("Random integer 1-100:", random.randint(1, 100))
print("Random choice:", random.choice(["apple", "banana", "cherry"]))

import datetime
print("\n--- Datetime Module ---")
print("Current date:", datetime.date.today())
print("Current time:", datetime.datetime.now().time())

# --------------------
# 5. __name__ == "__main__" (Important Concept)
# --------------------
# Put this at the bottom of your modules:

# if __name__ == "__main__":
#     print("This code runs only when the file is executed directly")
#     print("It does NOT run when the file is imported by another script")

# This prevents test code from running during imports.

# --------------------
# BEST PRACTICES
# --------------------
# - Keep each module focused on one purpose
# - Use meaningful file names (e.g., math_utils.py, file_handlers.py)
# - Prefer `from module import specific_function` for cleaner code
# - Avoid `from module import *` as it can cause naming conflicts
# - Modules make large programs much easier to manage

# Summary:
# - Modules = reusable .py files
# - `import module_name`
# - `from module_name import function_name`
# - Use `as` to create aliases
# - Standard library modules (math, random, datetime, etc.) are always available