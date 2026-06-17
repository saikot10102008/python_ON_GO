# Membership Operators in Python
# Membership operators test whether a value exists in a sequence (string, list, tuple, set, dict)
# Operators: 'in' and 'not in'

# --------------------
# EXAMPLE 1: Using 'in' with Strings
# --------------------
word = "APPLE"

# Test different letters (demonstration)
test_letters = ['A', 'P', 'L', 'X', 'a']

for letter in test_letters:
    if letter in word:
        print(f"There is a '{letter}' in '{word}'")
    else:
        print(f"'{letter}' was not found in '{word}'")

print()  # Blank line for readability

# --------------------
# EXAMPLE 2: Using 'in' with Sets (fast lookup)
# --------------------
students = {"Spongebob", "Patrick", "Sandy", "Mr. Krabs"}

test_students = ["Sandy", "Plankton", "Patrick"]

for student in test_students:
    if student in students:
        print(f"{student} is in this class")
    else:
        print(f"{student} is NOT in this class")

print()

# --------------------
# EXAMPLE 3: Using 'in' with Dictionaries (checks KEYS by default)
# --------------------
grades = {
    "Sandy": 'A',
    "Squidward": 'B',
    "Spongebob": 'C',
    "Patrick": 'D'
}

test_names = ["Sandy", "Gary", "Spongebob"]

for student in test_names:
    if student in grades:
        print(f"{student}'s grade is {grades[student]}")
    else:
        print(f"{student} is not in the dictionary")

print()

# --------------------
# EXAMPLE 4: Combining membership checks
# --------------------
email = "BroCode@gmail.com"

if "@" in email and "." in email:
    print("Valid email format")
else:
    print("Invalid email format")

# Checking for missing symbols
if "@" not in email:
    print("Missing @ symbol")

print()

# --------------------
# Additional Examples and Best Practices
# --------------------

my_list = [1, 2, 3, 4, 5]
print("List examples:")
print(3 in my_list)           # True
print(10 not in my_list)      # True
print()

my_tuple = ("apple", "banana", "cherry")
print("Tuple example:")
print("banana" in my_tuple)   # True
print()

# Case sensitivity with strings
print("Case sensitivity:")
print("Apple" in "apple pie")   # False
print("apple" in "apple pie")   # True
print()

# Summary of key points:
# - 'in' returns True if value is found
# - 'not in' returns True if value is NOT found
# - Works on: strings, lists, tuples, sets, dictionaries (keys)
# - Sets and dictionaries offer fastest membership testing
# - String checks are case-sensitive
# - Very useful for validation, searching, and control flow