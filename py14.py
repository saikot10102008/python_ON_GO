# IDENTITY OPERATORS IN PYTHON

# Identity operators check if two variables point to the SAME OBJECT in memory
# (not just if they have the same value)

# Two identity operators:
# 1. is      - Returns True if both variables are the SAME object
# 2. is not  - Returns True if both variables are NOT the same object

# -------------------------------------------------------------------
# EXAMPLE 1: Lists with same values but different objects
# -------------------------------------------------------------------

# Create three lists
a = [1, 2, 3]    # List 'a' in memory
b = a             # 'b' points to SAME object as 'a' (same memory location)
c = [1, 2, 3]     # 'c' has same values but is a DIFFERENT object in memory

print("a = [1, 2, 3]")
print("b = a (b points to same object as a)")
print("c = [1, 2, 3] (c is a new list with same values)")
print()

# Check identity
print("a is b     :", a is b)      # True - a and b are the SAME object
print("a is c     :", a is c)      # False - a and c are DIFFERENT objects
print("a is not c :", a is not c)  # True - a and c are not the same object
print()

# Check values (equality)
print("a == b     :", a == b)      # True - same values
print("a == c     :", a == c)      # True - same values
print()

# -------------------------------------------------------------------
# EXAMPLE 2: Numbers (special case)
# -------------------------------------------------------------------

# Python reuses small integers (-5 to 256) for efficiency
x = 10
y = 10
z = 1000
w = 1000

print("x = 10, y = 10")
print("z = 1000, w = 1000")
print()

print("x is y     :", x is y)      # True (small integers, same object)
print("z is w     :", z is w)      # False (large integers, different objects)
print()

# -------------------------------------------------------------------
# EXAMPLE 3: Strings (another special case)
# -------------------------------------------------------------------

str1 = "hello"
str2 = "hello"
str3 = "hello world"
str4 = "hello world"

print('str1 = "hello", str2 = "hello"')
print('str3 = "hello world", str4 = "hello world"')
print()

print("str1 is str2     :", str1 is str2)      # True (short strings are reused)
print("str3 is str4     :", str3 is str4)      # Usually True (Python interns strings)
print()

# -------------------------------------------------------------------
# EXAMPLE 4: None comparison (MOST COMMON USE)
# -------------------------------------------------------------------

# ALWAYS use 'is' or 'is not' when comparing with None
value = None

print("value = None")
print()

print("value is None     :", value is None)      # True - CORRECT way
print("value == None     :", value == None)      # True - but NOT recommended
print("value is not None :", value is not None)  # False
print()

# -------------------------------------------------------------------
# WHEN TO USE IDENTITY OPERATORS:
# -------------------------------------------------------------------

# 1. When checking if a variable is None (always use 'is' or 'is not')
# 2. When checking if two variables point to the same object in memory
# 3. When working with mutable objects (lists, dictionaries, sets)

# -------------------------------------------------------------------
# PRACTICE EXAMPLE:
# -------------------------------------------------------------------

# Create two identical lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1  # list3 points to same object as list1

print("list1 = [1, 2, 3]")
print("list2 = [1, 2, 3]")
print("list3 = list1")
print()

print("list1 is list2   :", list1 is list2)      # False (different objects)
print("list1 is list3   :", list1 is list3)      # True (same object)
print("list1 == list2   :", list1 == list2)      # True (same values)
print()

# -------------------------------------------------------------------
# QUICK REFERENCE:
# -------------------------------------------------------------------

print("=== QUICK REFERENCE ===")
print("Use 'is' when: Checking if SAME OBJECT in memory")
print("Use '==' when: Checking if VALUES are equal")
print()

# Most important rule:
print("ALWAYS use 'is' or 'is not' when comparing with None!")
print("Example: if x is None:   # CORRECT")
print("         if x == None:   # AVOID (works but not Pythonic)")