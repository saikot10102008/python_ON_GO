# ========================================================
# PYTHON OPERATORS 
# ========================================================

print("=== PYTHON OPERATORS NOTES (from the video section) ===")
print("Video timestamp: 59:11 to 01:39:27")
print("Operators are special symbols that perform operations on variables/values.\n")

# ========================================================
# 1. ARITHMETIC OPERATORS
# ========================================================
# These are used to perform mathematical operations.
# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division (always returns float)
# %   Modulus (remainder)
# **  Exponentiation (power)
# //  Floor Division (returns integer, rounds down)

a = 10
b = 3

print("Arithmetic Operators:")
print("10 + 3  =", a + b)      # 13
print("10 - 3  =", a - b)      # 7
print("10 * 3  =", a * b)      # 30
print("10 / 3  =", a / b)      # 3.333...
print("10 % 3  =", a % b)      # 1  (remainder)
print("10 ** 3 =", a ** b)     # 1000
print("10 // 3 =", a // b)     # 3  (floor division)
print("-" * 40)

# ========================================================
# 2. ASSIGNMENT OPERATORS
# ========================================================
# Used to assign values to variables.
# =    Simple assignment
# +=   Add and assign
# -=   Subtract and assign
# *=   Multiply and assign
# /=   Divide and assign
# %=   Modulus and assign
# **=  Exponent and assign
# //=  Floor division and assign

x = 5
print("Assignment Operators (starting with x = 5):")
x += 3   # same as x = x + 3
print("x += 3  →", x)   # 8

x -= 2
print("x -= 2  →", x)   # 6

x *= 4
print("x *= 4  →", x)   # 24

x /= 3
print("x /= 3  →", x)   # 8.0

x %= 5
print("x %= 5  →", x)   # 3.0

x **= 2
print("x **= 2 →", x)   # 9.0

x //= 2
print("x //= 2 →", x)   # 4.0
print("-" * 40)

# ========================================================
# 3. COMPARISON (RELATIONAL) OPERATORS
# ========================================================
# Used to compare two values. Returns True or False.
# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to

p = 10
q = 5

print("Comparison Operators:")
print("10 == 5  →", p == q)   # False
print("10 != 5  →", p != q)   # True
print("10 > 5   →", p > q)    # True
print("10 < 5   →", p < q)    # False
print("10 >= 5  →", p >= q)   # True
print("10 <= 5  →", p <= q)   # False
print("-" * 40)

# ========================================================
# 4. LOGICAL OPERATORS
# ========================================================
# Used to combine conditional statements.
# and  → True if both conditions are True
# or   → True if at least one condition is True
# not  → Reverses the result (True becomes False and vice versa)

r = 10
s = 5

print("Logical Operators:")
print("(r > s) and (r < 20)  →", (r > s) and (r < 20))   # True and True → True
print("(r > s) or (r < 5)    →", (r > s) or (r < 5))    # True or False → True
print("not (r > s)           →", not (r > s))           # not True → False
print("-" * 40)

# ========================================================
# 5. IDENTITY OPERATORS
# ========================================================
# Used to check if two objects are the same object (same memory location).
# is     → True if both variables point to the same object
# is not → True if both variables point to different objects

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("Identity Operators:")
print("list1 is list2     →", list1 is list2)      # False (different objects)
print("list1 is list3     →", list1 is list3)      # True (same object)
print("list1 is not list2 →", list1 is not list2)  # True
print("-" * 40)

# ========================================================
# 6. MEMBERSHIP OPERATORS
# ========================================================
# Used to test if a value is present in a sequence (string, list, tuple, etc.).
# in        → True if value is found in the sequence
# not in    → True if value is not found in the sequence

fruits = ["apple", "banana", "cherry"]

print("Membership Operators:")
print("'apple' in fruits        →", "apple" in fruits)      # True
print("'mango' in fruits       →", "mango" in fruits)     # False
print("'mango' not in fruits   →", "mango" not in fruits) # True
print("-" * 40)

# ========================================================
# 7. BITWISE OPERATORS
# ========================================================
# Work on bits (binary representation) of numbers.
# &   AND
# |   OR
# ^   XOR
# ~   NOT (inverts all bits)
# <<  Left shift
# >>  Right shift

m = 6   # binary: 110
n = 3   # binary: 011

print("Bitwise Operators:")
print("6 & 3  =", m & n)   # 2  (010)
print("6 | 3  =", m | n)   # 7  (111)
print("6 ^ 3  =", m ^ n)   # 5  (101)
print("~6     =", ~m)      # -7
print("6 << 1 =", m << 1)  # 12 (shift left by 1)
print("6 >> 1 =", m >> 1)  # 3  (shift right by 1)
print("-" * 40)

# ========================================================
# OPERATOR PRECEDENCE (BODMAS in Python)
# ========================================================
# Highest precedence first:
# () → ** → * / // % → + - → comparisons → not → and → or
# Always use parentheses for clarity!

result = 10 + 3 * 2 ** 2 - 5
print("Operator Precedence Example:")
print("10 + 3 * 2 ** 2 - 5 =", result)   # 10 + 3*4 - 5 = 17
print("With parentheses: (10 + 3) * (2 ** 2) - 5 =", (10 + 3) * (2 ** 2) - 5)
print("\n✅ End of Operators Notes")
print("Practice these in the video examples around 59:11 - 01:39:27")
print("Video recommends trying all examples yourself!")