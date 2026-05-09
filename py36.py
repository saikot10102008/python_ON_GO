"""
================================================================================
PYTHON DATA STRUCTURES - COMPREHENSIVE GUIDE WITH EXAMPLES
================================================================================

Data structures are specialized formats for organizing, managing, and storing data.
They define how data is arranged in memory and what operations can be performed.

Python provides several built-in data structures, each optimized for different use cases.
================================================================================
"""

# ============================================================================
# 1. LISTS - Ordered, mutable, allows duplicates
# ============================================================================

"""
Lists are the most commonly used data structure in Python.
- ORDERED: Elements maintain their position (index-based access)
- MUTABLE: Can be modified after creation (add, remove, change elements)
- ALLOWS DUPLICATES: Same value can appear multiple times
- HETEROGENEOUS: Can contain different data types
"""

# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True, None]
nested_list = [1, [2, 3], [4, [5, 6]]]

# Accessing list elements (0-indexed)
first = numbers[0]        # Access first element: 1
last = numbers[-1]        # Access last element: 5
range_access = numbers[1:4]  # Slice from index 1 to 3: [2, 3, 4]

# Modifying lists
numbers.append(6)         # Add element at end: [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)      # Insert at specific index: [0, 1, 2, 3, 4, 5, 6]
numbers.remove(3)         # Remove first occurrence of value 3
popped = numbers.pop()    # Remove and return last element
numbers.extend([7, 8, 9]) # Add multiple elements

# Common list operations
length = len(numbers)      # Get number of elements
reversed_list = numbers[::-1]  # Reverse using slicing
sorted_list = sorted(numbers)  # Return sorted copy (doesn't modify original)
numbers.sort()             # Sort in-place (modifies original)
count = numbers.count(2)   # Count occurrences of value
index = numbers.index(5)   # Find index of first occurrence

# List comprehension - concise way to create lists
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

print("Lists:")
print(f"  Original: {numbers}")
print(f"  Squares: {squares}")
print()


# ============================================================================
# 2. TUPLES - Ordered, immutable, allows duplicates
# ============================================================================

"""
Tuples are immutable sequences - once created, they cannot be changed.
- ORDERED: Elements maintain their position (index-based access)
- IMMUTABLE: Cannot be modified after creation (cannot add, remove, or change)
- ALLOWS DUPLICATES: Same value can appear multiple times
- FASTER & MEMORY EFFICIENT: More efficient than lists
- HASHABLE: Can be used as dictionary keys (if they contain only hashable items)
"""

# Creating tuples
empty_tuple = ()
single_element = (1,)      # Note: comma needed for single element
coordinates = (10, 20)
colors = ("red", "green", "blue")
mixed_tuple = (1, "hello", 3.14, True)

# Accessing tuple elements (same as lists)
first = colors[0]          # "red"
last = colors[-1]          # "blue"
partial = colors[0:2]      # ("red", "green")

# Tuple unpacking - assign elements to multiple variables
x, y = coordinates         # x = 10, y = 20
a, b, c = colors          # a = "red", b = "green", c = "blue"

# Immutability demonstration
# colors[0] = "yellow"     # This would raise TypeError!

# Tuple concatenation and repetition
new_tuple = colors + ("yellow",)  # Concatenate: ("red", "green", "blue", "yellow")
repeated = (1, 2) * 3             # Repeat: (1, 2, 1, 2, 1, 2)

# Common tuple operations
length = len(colors)       # Get number of elements: 3
count = colors.count("red")  # Count occurrences: 1
index = colors.index("green")  # Find index: 1

# Converting between list and tuple
list_to_tuple = tuple([1, 2, 3])     # (1, 2, 3)
tuple_to_list = list((1, 2, 3))      # [1, 2, 3]

print("Tuples:")
print(f"  Colors: {colors}")
print(f"  Unpacked: x={x}, y={y}")
print()


# ============================================================================
# 3. DICTIONARIES - Unordered, mutable, key-value pairs
# ============================================================================

"""
Dictionaries store data as key-value pairs.
- UNORDERED (Python 3.7+): Insertion order is maintained, but not the primary feature
- MUTABLE: Can be modified after creation
- KEY-VALUE PAIRS: Access values using keys (not indices)
- KEYS MUST BE UNIQUE: Each key appears only once
- KEYS MUST BE HASHABLE: Keys are usually strings, numbers, or tuples
- VALUES CAN BE ANYTHING: Values can be any data type, including duplicates
"""

# Creating dictionaries
empty_dict = {}
student = {"name": "John", "age": 20, "grade": "A"}
numbers_dict = {1: "one", 2: "two", 3: "three"}
nested_dict = {
    "student1": {"name": "Alice", "age": 21},
    "student2": {"name": "Bob", "age": 22}
}

# Accessing dictionary values
name = student["name"]     # "John" (using key)
age = student.get("age")   # 20 (safer method, returns None if key doesn't exist)
default_value = student.get("address", "Not provided")  # Default if key missing

# Modifying dictionaries
student["age"] = 21        # Update existing value
student["address"] = "123 Main St"  # Add new key-value pair
student.update({"city": "New York", "country": "USA"})  # Add multiple pairs

# Removing from dictionaries
del student["address"]     # Delete specific key
removed_value = student.pop("city")  # Remove and return value
student.clear()            # Remove all items

# Recreating student for remaining examples
student = {"name": "John", "age": 20, "grade": "A", "city": "New York"}

# Dictionary operations
keys = student.keys()      # Get all keys: dict_keys(['name', 'age', 'grade', 'city'])
values = student.values()  # Get all values: dict_values(['John', 20, 'A', 'New York'])
items = student.items()    # Get key-value pairs: dict_items([('name', 'John'), ...])

# Iterating through dictionaries
for key in student:        # Iterate through keys
    print(f"{key}: {student[key]}")

for key, value in student.items():  # Iterate through key-value pairs
    pass

# Dictionary comprehension - create dictionaries concisely
squares_dict = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Check if key exists
if "name" in student:      # True
    print(student["name"])

print("Dictionaries:")
print(f"  Student: {student}")
print(f"  Squares: {squares_dict}")
print()


# ============================================================================
# 4. SETS - Unordered, mutable, no duplicates
# ============================================================================

"""
Sets are collections of unique, unordered elements.
- UNORDERED: No index-based access, order is not guaranteed
- MUTABLE: Can be modified after creation
- NO DUPLICATES: Each element appears only once (duplicates are automatically removed)
- FAST LOOKUPS: Optimized for membership testing (checking if element exists)
- HASHABLE ELEMENTS: Can only contain hashable items (no lists or dictionaries)
"""

# Creating sets
empty_set = set()          # Note: {} creates a dict, not a set
numbers_set = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14, True}
from_list = set([1, 2, 2, 3, 3, 3])  # Duplicates removed: {1, 2, 3}

# Note: You cannot access elements by index in sets
# numbers_set[0]  # This would raise TypeError!

# Modifying sets
numbers_set.add(6)         # Add single element: {1, 2, 3, 4, 5, 6}
numbers_set.update([7, 8, 9])  # Add multiple elements
numbers_set.remove(5)      # Remove element (raises error if not found)
numbers_set.discard(100)   # Remove element (no error if not found)
popped = numbers_set.pop() # Remove and return arbitrary element

# Set operations (mathematical set operations)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

union = set_a | set_b      # Combine all elements: {1, 2, 3, 4, 5, 6}
intersection = set_a & set_b  # Common elements: {3, 4}
difference = set_a - set_b    # Elements in set_a but not in set_b: {1, 2}
symmetric_diff = set_a ^ set_b  # Elements in either but not both: {1, 2, 5, 6}

# Alternative method names for set operations
union2 = set_a.union(set_b)
intersection2 = set_a.intersection(set_b)
difference2 = set_a.difference(set_b)

# Checking membership
if 3 in set_a:             # True
    print("3 is in set_a")

# Set comprehension
even_set = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}

# Frozen sets - immutable version of sets
frozen = frozenset([1, 2, 3])  # Cannot be modified
# frozen.add(4)  # This would raise AttributeError!

print("Sets:")
print(f"  Set A: {set_a}")
print(f"  Set B: {set_b}")
print(f"  Union: {union}")
print(f"  Intersection: {intersection}")
print()


# ============================================================================
# 5. STRINGS - Ordered, immutable, sequence of characters
# ============================================================================

"""
Strings are sequences of characters.
- ORDERED: Characters maintain their position (index-based access)
- IMMUTABLE: Cannot be modified after creation
- SEQUENCE: Can be indexed, sliced, and iterated
- INDEXABLE & SLICEABLE: Same operations as lists and tuples
"""

# Creating strings
empty_string = ""
simple_string = "Hello, World!"
multiline_string = """This is a
multiline string that spans
multiple lines"""
raw_string = r"C:\Users\Name\file.txt"  # Raw string (backslashes not escaped)

# Accessing string characters (0-indexed)
first_char = simple_string[0]      # "H"
last_char = simple_string[-1]      # "!"
substring = simple_string[0:5]     # "Hello"

# String immutability demonstration
# simple_string[0] = "h"  # This would raise TypeError!

# String concatenation
greeting = "Hello" + " " + "World"  # "Hello World"
repeated = "Ha" * 3                 # "HaHaHa"

# String operations
length = len(simple_string)         # Get number of characters
upper = simple_string.upper()       # "HELLO, WORLD!"
lower = simple_string.lower()       # "hello, world!"
title = simple_string.title()       # "Hello, World!"

# String methods
is_digit = "123".isdigit()          # True
is_alpha = "abc".isalpha()          # True
is_alnum = "abc123".isalnum()       # True

# String searching and replacing
index = simple_string.find("World")  # Find index: 7
count = simple_string.count("l")     # Count occurrences: 3
replaced = simple_string.replace("World", "Python")  # Replace substring

# Splitting and joining
words = simple_string.split()        # Split by whitespace: ['Hello,', 'World!']
numbers_split = "1,2,3,4".split(",")  # Split by delimiter: ['1', '2', '3', '4']
rejoined = "-".join(["a", "b", "c"])  # Join with delimiter: "a-b-c"

# String formatting
name = "Alice"
age = 25
formatted1 = f"Name: {name}, Age: {age}"  # f-string (Python 3.6+)
formatted2 = "Name: {}, Age: {}".format(name, age)  # .format()
formatted3 = "Name: %s, Age: %d" % (name, age)  # % formatting (older)

# Trimming whitespace
text = "  Hello  "
trimmed = text.strip()              # "Hello" (remove leading/trailing)
left_trim = text.lstrip()           # "Hello  "
right_trim = text.rstrip()          # "  Hello"

print("Strings:")
print(f"  Original: {simple_string}")
print(f"  Upper: {upper}")
print(f"  Formatted: {formatted1}")
print()


# ============================================================================
# 6. COLLECTIONS MODULE - Specialized data structures
# ============================================================================

"""
The collections module provides additional data structures optimized for
specific use cases.
"""

from collections import Counter, defaultdict, deque, namedtuple

# Counter - Count occurrences of elements
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)        # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
most_common = word_count.most_common(2)  # [('apple', 3), ('banana', 2)]

# defaultdict - Dictionary with default values for missing keys
def_dict = defaultdict(list)
def_dict["fruits"].append("apple")   # No KeyError, automatically creates list
def_dict["fruits"].append("banana")  # [apple, banana]

# deque - Double-ended queue, optimized for adding/removing from both ends
queue = deque([1, 2, 3])
queue.append(4)                      # Add to right: deque([1, 2, 3, 4])
queue.appendleft(0)                  # Add to left: deque([0, 1, 2, 3, 4])
queue.pop()                          # Remove from right: 4
queue.popleft()                      # Remove from left: 0

# namedtuple - Tuple with named fields (more readable than regular tuples)
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(f"Point: x={p.x}, y={p.y}")    # More readable than p[0], p[1]

print("Collections:")
print(f"  Word count: {word_count}")
print(f"  Deque: {queue}")
print()


# ============================================================================
# 7. COMPARISON OF DATA STRUCTURES
# ============================================================================

"""
CHOOSING THE RIGHT DATA STRUCTURE:

LIST:
  - Use when: You need ordered, mutable collection with index access
  - Pros: Flexible, supports various operations, good for general use
  - Cons: Slower than tuples, not hashable

TUPLE:
  - Use when: You need immutable, ordered collection or hashable key
  - Pros: Faster than lists, memory efficient, can be dictionary keys
  - Cons: Cannot be modified after creation

DICTIONARY:
  - Use when: You need key-value associations with fast lookup
  - Pros: Fast lookups by key, flexible, mutable
  - Cons: Unordered (though insertion order preserved in Python 3.7+)

SET:
  - Use when: You need unique elements and fast membership testing
  - Pros: Fast lookups, automatically removes duplicates, set operations
  - Cons: Unordered, cannot contain mutable objects

STRING:
  - Use when: You need to store and manipulate text
  - Pros: Immutable, many useful methods, universal text representation
  - Cons: Cannot modify individual characters (must create new string)

DEQUE:
  - Use when: You need efficient add/remove from both ends
  - Pros: O(1) operations on both ends
  - Cons: Less efficient for random access

COUNTER:
  - Use when: You need to count element occurrences
  - Pros: Convenient, fast, built-in most common functionality
  - Cons: Only for counting, not general storage
"""

# Time Complexity Comparison (approximate)
complexity_table = """
OPERATION              LIST        TUPLE       DICT        SET
Access by index        O(1)        O(1)        -           -
Search                 O(n)        O(n)        O(1)*       O(1)*
Insert                 O(n)        -           O(1)*       O(1)*
Delete                 O(n)        -           O(1)*       O(1)*
Copy                   O(n)        O(n)        O(n)        O(n)

* Average case; worst case can be O(n)
- = operation not applicable
"""

print("Data Structure Complexity:")
print(complexity_table)


# ============================================================================
# 8. PRACTICAL EXAMPLES
# ============================================================================

# Example 1: Store student information
students = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 88]},
    {"name": "Bob", "age": 21, "grades": [75, 80, 82]},
    {"name": "Charlie", "age": 20, "grades": [95, 92, 98]},
]

# Example 2: Unique tags from multiple posts
tags_set = set()
posts = [
    {"title": "Python basics", "tags": ["python", "programming", "tutorial"]},
    {"title": "Web dev", "tags": ["python", "django", "web"]},
    {"title": "Data analysis", "tags": ["python", "pandas", "data"]},
]
for post in posts:
    tags_set.update(post["tags"])

# Example 3: Word frequency counter
text = "the quick brown fox jumps over the lazy dog"
word_freq = Counter(text.split())

# Example 4: Cache using dictionary
cache = {}
def fibonacci(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    result = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = result
    return result

print("Practical Examples:")
print(f"  Students: {len(students)} records")
print(f"  Unique tags: {tags_set}")
print(f"  Word frequency: {word_freq}")
print()

# ============================================================================
# SUMMARY
# ============================================================================

print("=" * 80)
print("KEY TAKEAWAYS:")
print("=" * 80)
print("""
1. LISTS - Mutable ordered sequences (most flexible)
2. TUPLES - Immutable ordered sequences (faster, hashable)
3. DICTIONARIES - Key-value pairs (fast lookups)
4. SETS - Unique unordered elements (no duplicates)
5. STRINGS - Immutable sequences of characters (text)
6. Special structures in collections module for specific needs

Choose based on your specific needs:
- Need to modify? → List or Dict or Set
- Need immutable? → Tuple or String or frozenset
- Need key-value pairs? → Dictionary
- Need unique items? → Set
- Need text? → String
- Need both ends efficiency? → deque
- Need to count? → Counter
""")
