# ========================================================
# TYPE CONVERSION IN PYTHON - ELABORATE EXPLANATION
# ========================================================

print("=== TYPE CONVERSION IN PYTHON - FULL GUIDE ===\n")

# ========================================================
# 1. WHAT IS TYPE CONVERSION?
# ========================================================
# Type conversion means changing the data type of a value
# from one type to another (e.g., string → integer).
#
# Why do we need it?
# - Python is strictly typed during operations.
# - You cannot directly add string + integer without conversion.
# - It helps in user input (always comes as string), data cleaning,
#   API responses, file reading, etc.
#
# Two main categories:
#   A) IMPLICIT TYPE CONVERSION (Automatic by Python)
#   B) EXPLICIT TYPE CONVERSION (Manual by programmer)

# ========================================================
# 2. IMPLICIT TYPE CONVERSION (Automatic)
# ========================================================
# Python automatically converts a "smaller" data type to a
# "larger" data type during arithmetic operations to prevent
# data loss. This is also called "type coercion".

print("=== 2. IMPLICIT CONVERSION ===")

a = 10          # int
b = 5.5         # float
result1 = a + b
print(f"int({a}) + float({b}) → {result1} (type: {type(result1)})")

# Another example with complex
c = 3 + 2j      # complex
result2 = a + c
print(f"int({a}) + complex({c}) → {result2} (type: {type(result2)})")

# Important points about implicit:
# - Only happens in arithmetic, comparison, logical operations.
# - Never converts to a smaller type (e.g., float never → int automatically).
# - Helps avoid "TypeError" in mixed-type operations.

# ========================================================
# 3. EXPLICIT TYPE CONVERSION (Manual Casting)
# ========================================================
# You use built-in functions to force conversion.
# Syntax: target_type(value)

print("\n=== 3. EXPLICIT CONVERSION ===")

# ----------------------------------------------------
# 3.1 String ↔ Number conversions (most common)
print("3.1 String ↔ Number")

# String → Integer
user_input = "2026"
year = int(user_input)
print(f"str → int : '{user_input}' → {year} (type: {type(year)})")

# String → Float
price_str = "99.99"
price = float(price_str)
print(f"str → float : '{price_str}' → {price} (type: {type(price)})")

# Integer/Float → String (very useful for concatenation)
age = 25
age_str = str(age)
print(f"int → str : {age} → '{age_str}' (type: {type(age_str)})")

# Warning:
# - int("123.45") will FAIL → ValueError
# - float("abc") will FAIL → ValueError
# - Always handle exceptions in real code!

# ----------------------------------------------------
# 3.2 Number → Integer (truncation, NOT rounding)
print("\n3.2 Number → Integer")

print(f"float 7.9  → int → {int(7.9)}")      # truncates decimal
print(f"float 7.1  → int → {int(7.1)}")
print(f"float -3.8 → int → {int(-3.8)}")     # towards zero

# ----------------------------------------------------
# 3.3 Any type → Boolean (Truthiness rules)
print("\n3.3 Any → Boolean")

print(f"bool(0)      → {bool(0)}")          # False
print(f"bool(1)      → {bool(1)}")          # True
print(f"bool(-5)     → {bool(-5)}")         # True
print(f"bool(0.0)    → {bool(0.0)}")        # False
print(f"bool('')     → {bool('')}")         # False (empty string)
print(f"bool('hello')→ {bool('hello')}")    # True
print(f"bool([])     → {bool([])}")         # False (empty list)
print(f"bool([1])    → {bool([1])}")        # True
print(f"bool(None)   → {bool(None)}")       # False

# Rule of thumb:
# → False: 0, 0.0, "", '', [], (), {}, None, False
# → True:  Everything else

# ----------------------------------------------------
# 3.4 Collection conversions
print("\n3.4 Collection Conversions")

lst = [1, 2, 2, 3]
print(f"list → tuple : {tuple(lst)}")
print(f"list → set   : {set(lst)}")         # removes duplicates

tup = (10, 20, 30)
print(f"tuple → list : {list(tup)}")

# Dictionary conversions
d = {"a": 1, "b": 2}
print(f"dict → list (keys)   : {list(d)}")
print(f"dict → list (items)  : {list(d.items())}")

# String → List of characters
name = "Python"
print(f"str → list : {list(name)}")

# ----------------------------------------------------
# 3.5 Advanced / Less common conversions
print("\n3.5 Advanced Conversions")

# int → complex
print(f"int → complex : {complex(5)}")           # 5+0j
print(f"int → complex with imag : {complex(5, 3)}")  # 5+3j

# chr() and ord() - character ↔ integer (ASCII/Unicode)
print(f"ord('A')  → {ord('A')}")   # 65
print(f"chr(65)   → {chr(65)}")    # 'A'

# bin(), oct(), hex()
print(f"bin(10) → {bin(10)}")      # 0b1010
print(f"oct(10) → {oct(10)}")      # 0o12
print(f"hex(10) → {hex(10)}")      # 0xa

# ========================================================
# 4. COMMON PITFALLS & BEST PRACTICES
# ========================================================
print("\n=== 4. COMMON PITFALLS & BEST PRACTICES ===")

# Pitfall 1: Trying to convert invalid data
# Uncomment to see error:
# int("hello")          # → ValueError

# Pitfall 2: Floating point precision after conversion
f = 0.1 + 0.2
print(f"0.1 + 0.2 = {f} (float)")
print(f"int(0.1 + 0.2) = {int(f)}")   # 0 (because 0.30000000000000004)

# Best Practice: Always validate before conversion
def safe_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        print(f"Cannot convert '{value}' to int")
        return None

print(f"safe_int('123') → {safe_int('123')}")
print(f"safe_int('abc')  → {safe_int('abc')}")

# Best Practice: Use explicit conversion even when implicit works
# → makes code more readable and predictable.

# ========================================================
# 5. SUMMARY TABLE (in comments)
# ========================================================
# Function     | Converts from          | Converts to
# ---------------------------------------------------
# int()        | str, float, bool       | integer
# float()      | str, int, bool         | floating point
# str()        | any                    | string
# bool()       | any                    | True/False
# list()       | tuple, set, str, dict  | list
# tuple()      | list, set, str         | tuple
# set()        | list, tuple, str       | set
# dict()       | list of tuples         | dictionary
# complex()    | int, float, str        | complex
# chr(), ord() | int <-> str (char)     | character

print("\n=== END OF ELABORATE TYPE CONVERSION GUIDE ===")
print("Run this file to see all examples in action!")
print("Save as type_conversion_elaborate.py and experiment!")