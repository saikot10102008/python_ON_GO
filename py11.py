# =============================================================================
# COMPARISON OPERATORS IN PYTHON
# =============================================================================

# Comparison operators are used to compare two values and return a Boolean:
# - True if the comparison is correct
# - False if the comparison is incorrect

# -----------------------------------------------------------------------------
# LIST OF ALL COMPARISON OPERATORS
# -----------------------------------------------------------------------------

# 1. ==  (Equal to)          : Checks if two values are equal
# 2. !=  (Not equal to)      : Checks if two values are NOT equal
# 3. >   (Greater than)      : Checks if left value is greater than right value
# 4. <   (Less than)         : Checks if left value is less than right value
# 5. >=  (Greater than or equal to) : Checks if left value is greater than OR equal to right value
# 6. <=  (Less than or equal to)    : Checks if left value is less than OR equal to right value

# -----------------------------------------------------------------------------
# EXAMPLE 1: BASIC NUMERIC COMPARISONS
# -----------------------------------------------------------------------------

print("=== EXAMPLE 1: BASIC NUMERIC COMPARISONS ===")

# Define two variables for comparison
x = 10
y = 5

print(f"Let's compare: x = {x}, y = {y}")
print()

# 1. EQUAL TO (==)
print("1. EQUAL TO (==)")
print(f"   x == y  : {x} == {y}  -> {x == y}")  # 10 == 5  -> False
print(f"   x == 10 : {x} == 10  -> {x == 10}")  # 10 == 10 -> True
print()

# 2. NOT EQUAL TO (!=)
print("2. NOT EQUAL TO (!=)")
print(f"   x != y  : {x} != {y}  -> {x != y}")  # 10 != 5  -> True
print(f"   x != 10 : {x} != 10  -> {x != 10}")  # 10 != 10 -> False
print()

# 3. GREATER THAN (>)
print("3. GREATER THAN (>)")
print(f"   x > y   : {x} > {y}   -> {x > y}")  # 10 > 5   -> True
print(f"   y > x   : {y} > {x}   -> {y > x}")  # 5 > 10   -> False
print()

# 4. LESS THAN (<)
print("4. LESS THAN (<)")
print(f"   x < y   : {x} < {y}   -> {x < y}")  # 10 < 5   -> False
print(f"   y < x   : {y} < {x}   -> {y < x}")  # 5 < 10   -> True
print()

# 5. GREATER THAN OR EQUAL TO (>=)
print("5. GREATER THAN OR EQUAL TO (>=)")
print(f"   x >= y  : {x} >= {y}  -> {x >= y}")  # 10 >= 5  -> True
print(f"   x >= 10 : {x} >= 10  -> {x >= 10}")  # 10 >= 10 -> True
print(f"   y >= x  : {y} >= {x}  -> {y >= x}")  # 5 >= 10  -> False
print()

# 6. LESS THAN OR EQUAL TO (<=)
print("6. LESS THAN OR EQUAL TO (<=)")
print(f"   x <= y  : {x} <= {y}  -> {x <= y}")  # 10 <= 5  -> False
print(f"   x <= 10 : {x} <= 10  -> {x <= 10}")  # 10 <= 10 -> True
print(f"   y <= x  : {y} <= {x}  -> {y <= x}")  # 5 <= 10  -> True

# -----------------------------------------------------------------------------
# EXAMPLE 2: STRING COMPARISONS
# -----------------------------------------------------------------------------

print("\n=== EXAMPLE 2: STRING COMPARISONS ===")

name1 = "Alice"
name2 = "Bob"
name3 = "Alice"

print(f"name1 = '{name1}', name2 = '{name2}', name3 = '{name3}'")
print()

# Strings are compared alphabetically (lexicographically)
print(f"name1 == name2 : '{name1}' == '{name2}' -> {name1 == name2}")  # False
print(f"name1 == name3 : '{name1}' == '{name3}' -> {name1 == name3}")  # True
print(f"name1 != name2 : '{name1}' != '{name2}' -> {name1 != name2}")  # True

# Alphabetical order comparisons
print(f"'apple' < 'banana' : 'apple' < 'banana' -> {'apple' < 'banana'}")  # True
print(f"'cat' > 'dog'      : 'cat' > 'dog'      -> {'cat' > 'dog'}")  # False

# Case matters in string comparisons (uppercase < lowercase in ASCII)
print(f"'A' < 'a' : 'A' < 'a' -> {'A' < 'a'}")  # True (ASCII: A=65, a=97)

# -----------------------------------------------------------------------------
# EXAMPLE 3: REAL-WORLD USAGE
# -----------------------------------------------------------------------------

print("\n=== EXAMPLE 3: REAL-WORLD USAGE ===")

# Age verification for voting
age = 20
voting_age = 18

print(f"Age: {age}, Voting age: {voting_age}")
print(f"Can vote? age >= voting_age : {age} >= {voting_age} -> {age >= voting_age}")

# Password validation
entered_password = "secret123"
stored_password = "secret123"

print("\n Password check:")
print(
    f"Passwords match? entered_password == stored_password -> {entered_password == stored_password}"
)

# Temperature check
temperature = 25.5
freezing_point = 0.0
boiling_point = 100.0

print(f"\nTemperature: {temperature}°C")
print(
    f"Is freezing? temperature <= freezing_point : {temperature} <= {freezing_point} -> {temperature <= freezing_point}"
)
print(
    f"Is boiling? temperature >= boiling_point : {temperature} >= {boiling_point} -> {temperature >= boiling_point}"
)

# -----------------------------------------------------------------------------
# EXAMPLE 4: COMMON MISTAKES TO AVOID
# -----------------------------------------------------------------------------

print("\n=== EXAMPLE 4: COMMON MISTAKES ===")

# MISTAKE 1: Using = (assignment) instead of == (comparison)
# WRONG: if x = 10:   # This will cause an error
# CORRECT: if x == 10:

# MISTAKE 2: Comparing different data types
print(f"10 == '10' : {10 == '10'}")  # False - integer vs string
print(f"10 == 10.0 : {10 == 10.0}")  # True - int vs float (same value)

# MISTAKE 3: Chaining comparisons (Python actually allows this!)
print("\nPython allows chained comparisons:")
print(f"5 < 10 < 15 : {5 < 10 < 15}")  # True (equivalent to: 5 < 10 and 10 < 15)

# -----------------------------------------------------------------------------
# QUICK REFERENCE TABLE
# -----------------------------------------------------------------------------

print("\n=== QUICK REFERENCE TABLE ===")
print("| Operator | Name                     | Example  | Result  |")
print("|----------|--------------------------|----------|---------|")
print(f"|    ==    | Equal to                | 5 == 5   | {5 == 5}  |")
print(f"|    !=    | Not equal to            | 5 != 3   | {5 != 3}  |")
print(f"|    >     | Greater than            | 5 > 3    | {5 > 3}   |")
print(f"|    <     | Less than               | 5 < 3    | {5 < 3}   |")
print(f"|    >=    | Greater than or equal to| 5 >= 5   | {5 >= 5}  |")
print(f"|    <=    | Less than or equal to   | 5 <= 3   | {5 <= 3}  |")

# -----------------------------------------------------------------------------
# PRACTICE EXERCISE
# -----------------------------------------------------------------------------

print("\n=== PRACTICE EXERCISE ===")

# Try to predict the output before running
a = 15
b = 20
c = 15

print(f"Given: a = {a}, b = {b}, c = {c}")
print("Predict the results:")

print(f"\n1. a == b : {a} == {b} = ?")
print(f"2. a != b : {a} != {b} = ?")
print(f"3. a > b  : {a} > {b} = ?")
print(f"4. a < b  : {a} < {b} = ?")
print(f"5. a >= c : {a} >= {c} = ?")
print(f"6. b <= c : {b} <= {c} = ?")

# Uncomment to see answers:
# print("\n--- Answers ---")
# print(f"1. a == b : {a} == {b} = {a == b}")
# print(f"2. a != b : {a} != {b} = {a != b}")
# print(f"3. a > b  : {a} > {b} = {a > b}")
# print(f"4. a < b  : {a} < {b} = {a < b}")
# print(f"5. a >= c : {a} >= {c} = {a >= c}")
# print(f"6. b <= c : {b} <= {c} = {b <= c}")

print("\n" + "=" * 60)
print("Remember: Comparison operators always return True or False!")
print("Use them to make decisions in if statements and loops.")
print("=" * 60)
