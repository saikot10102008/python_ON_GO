# Python Scope - Made Super Easy & Detailed
# Scope = The region of your code where a variable can be accessed.
# Think of scope like "visibility zones" or "rooms" in a house.
# A variable declared in one room may or may not be visible in another room.

# Python uses LEGB rule to find variables:
# L → Local
# E → Enclosing (parent function)
# G → Global
# B → Built-in

print("=== UNDERSTANDING SCOPE IN PYTHON ===\n")

# --------------------
# 1. LOCAL SCOPE (Most Inner Room)
# --------------------
# Variables created inside a function are LOCAL.
# They only exist while the function is running.
# Once the function ends, they are destroyed (forgotten).

def my_func():
    local_variable = "I only exist inside this function!"
    print("Inside function:", local_variable)

my_func()

# Trying to access it outside will cause an error:
# print(local_variable)   # NameError: not defined

print("-" * 40)


# --------------------
# 2. GLOBAL SCOPE (The Whole House)
# --------------------
# Variables created outside any function are GLOBAL.
# They can be read from anywhere in the file.

global_name = "Bro Code"   # This is a global variable

def greet():
    print("Hello from inside function:", global_name)   # Can read global

greet()
print("Outside function:", global_name)

print("-" * 40)


# --------------------
# 3. MODIFYING A GLOBAL VARIABLE INSIDE A FUNCTION
# --------------------
# By default, Python creates a new local variable if you assign inside a function.
# To modify the real global variable, use the 'global' keyword.

count = 0

def increment_count():
    global count          # Tell Python: "Use the global count, don't make a new one"
    count = count + 1
    print("Count inside function:", count)

increment_count()
increment_count()
increment_count()
print("Final count outside:", count)

print("-" * 40)


# --------------------
# 4. ENCLOSING SCOPE (Nested Functions)
# --------------------
# When you have a function inside another function.
# The inner function can access variables from the outer function.

def outer():
    outer_var = "I belong to the outer function"
    
    def inner():
        nonlocal outer_var      # 'nonlocal' says: use the outer function's variable
        outer_var = "Modified by the inner function!"
        print("Inside inner function:", outer_var)
    
    inner()
    print("Back in outer function:", outer_var)

outer()

print("-" * 40)


# --------------------
# 5. BUILT-IN SCOPE (Python's Default Tools)
# --------------------
# These are functions and names that Python provides by default.
# Examples: print(), len(), range(), max(), etc.

print("This is using built-in 'print' function")
print("Length of list:", len([10, 20, 30, 40]))
print("Maximum number:", max(5, 12, 3))

print("-" * 40)


# --------------------
# 6. LEGB RULE - HOW PYTHON SEARCHES FOR VARIABLES
# --------------------
# Order of searching:
# 1. Local (inside current function)
# 2. Enclosing (outer functions)
# 3. Global (top level of file)
# 4. Built-in (Python's built-ins)

name = "Global Level"          # Global

def outer_function():
    name = "Enclosing Level"   # Enclosing
    
    def inner_function():
        name = "Local Level"   # Local
        print("Inside inner:", name)   # Looks at Local first → "Local Level"
    
    inner_function()
    print("Inside outer:", name)       # Enclosing level

outer_function()
print("Outside everything:", name)     # Global level

print("-" * 40)


# --------------------
# COMMON MISTAKES & BEST PRACTICES
# --------------------

x = 100

def wrong_example():
    x = 200          # This creates a NEW local variable!
    print("Inside function:", x)

wrong_example()
print("Outside function (still global):", x)   # Remains 100

# Best way: Avoid modifying globals when possible.
# Instead, pass values as arguments and return results.

def good_example(num):
    num = num + 50
    return num

result = good_example(x)
print("Better approach result:", result)

print("-" * 40)

# --------------------
# SUMMARY - EASY TO REMEMBER
# --------------------
# - Local: Inside the current function (smallest room)
# - Enclosing: In the outer function (bigger room)
# - Global: At the top of your file (the whole house)
# - Built-in: Python's own tools (outside the house)

# LEGB = Local → Enclosing → Global → Built-in
# Always try to use the smallest scope possible for your variables.
# This makes your code safer and easier to understand.

print("Scope lesson completed! 🎉")