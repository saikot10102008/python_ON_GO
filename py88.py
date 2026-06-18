# List Comprehensions in Python
# List comprehension provides a concise way to create lists.
# Syntax: [expression for value in iterable if condition]

# --------------------
# BASIC LIST COMPREHENSION
# --------------------

# Traditional way
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)
print("Doubles (traditional):", doubles)

# Using list comprehension
doubles = [x * 2 for x in range(1, 11)]
print("Doubles (comprehension):", doubles)

# --------------------
# WITH CONDITIONAL (IF only)
# --------------------

# Only even numbers
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers:", evens)

# Only fruits containing 'a'
fruits = ["apple", "orange", "banana", "coconut"]
fruits_with_a = [fruit for fruit in fruits if 'a' in fruit]
print("Fruits with 'a':", fruits_with_a)

# --------------------
# USING ELSE - CONDITIONAL EXPRESSION
# --------------------
# Syntax: [value_if_true if condition else value_if_false for item in iterable]

# Example: Label numbers as Even or Odd
parity = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 11)]
print("Even/Odd labels:", parity)

# Example: Positive or Negative
numbers = [-5, 3, -2, 7, -1, 8, 0]
signs = ["Positive" if n > 0 else "Negative" if n < 0 else "Zero" for n in numbers]
print("Signs:", signs)

# Example: Keep number if positive, else replace with 0
positive_or_zero = [num if num > 0 else 0 for num in numbers]
print("Positive or zero:", positive_or_zero)

# Example with strings
words = ["hello", "WORLD", "python", "CODE"]
normalized = [word.lower() if word.isupper() else word.upper() for word in words]
print("Normalized words:", normalized)

# --------------------
# MORE EXAMPLES
# --------------------

# Squares of numbers, but "N/A" for odd numbers
squares_or_na = [x*x if x % 2 == 0 else "N/A" for x in range(1, 11)]
print("Squares or N/A:", squares_or_na)

# --------------------
# NESTED LIST COMPREHENSIONS
# --------------------

multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("Multiplication table:")
for row in multiplication_table:
    print(row)

# --------------------
# DICTIONARY & SET COMPREHENSIONS
# --------------------

squared_dict = {x: x*x for x in range(6)}
print("Squared dict:", squared_dict)

unique_squares = {x*x for x in range(10)}
print("Unique squares set:", unique_squares)

# --------------------
# SUMMARY & BEST PRACTICES
# --------------------

# 1. Simple list comprehension:
#    [expression for item in iterable]

# 2. With filter (if only):
#    [expression for item in iterable if condition]

# 3. With if-else (ternary):
#    [value_if_true if condition else value_if_false for item in iterable]

# Note: The 'else' part must come BEFORE the 'for' keyword when used.

# List comprehensions are:
# - More readable for simple operations
# - Generally faster than traditional for loops
# - Pythonic and widely used

# Keep comprehensions clean. If logic gets too complex, use a normal for loop instead.