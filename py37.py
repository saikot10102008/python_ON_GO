# ============================================================
# PYTHON LISTS - DETAILED NOTES (WITH EXAMPLES)
# ============================================================

# A list is a built-in Python data type used to store multiple values.
# Key properties:
# 1) Ordered   -> items keep their position.
# 2) Mutable   -> you can change items after creation.
# 3) Duplicates allowed -> same value can appear multiple times.
# 4) Mixed types allowed -> numbers, strings, booleans, lists, etc.


# ------------------------------------------------------------
# 1) Creating lists
# ------------------------------------------------------------
# You can create a list using square brackets [] or list().
numbers = [10, 20, 30, 40]
mixed = [1, "hello", True, 3.14]
chars = list("abc")  # Converts each character to a list item

print("numbers:", numbers)
print("mixed:", mixed)
print("chars:", chars)


# ------------------------------------------------------------
# 2) Indexing (accessing list items)
# ------------------------------------------------------------
# Positive index starts from 0.
# Negative index starts from -1 (from the end).
colors = ["red", "green", "blue", "yellow"]

print("first color (index 0):", colors[0])
print("third color (index 2):", colors[2])
print("last color (index -1):", colors[-1])


# ------------------------------------------------------------
# 3) Slicing (getting a part of a list)
# ------------------------------------------------------------
# Syntax: list[start:stop:step]
# start is inclusive, stop is exclusive.
nums = [0, 1, 2, 3, 4, 5, 6]

print("nums[1:5] ->", nums[1:5])    # [1, 2, 3, 4]
print("nums[:4] ->", nums[:4])      # [0, 1, 2, 3]
print("nums[3:] ->", nums[3:])      # [3, 4, 5, 6]
print("nums[::2] ->", nums[::2])    # [0, 2, 4, 6]
print("nums[::-1] ->", nums[::-1])  # reversed copy


# ------------------------------------------------------------
# 4) Updating list items
# ------------------------------------------------------------
# Because lists are mutable, we can change values directly.
letters = ["A", "B", "C"]
letters[1] = "Z"
print("updated letters:", letters)

# Slice assignment can replace multiple items.
data = [1, 2, 3, 4, 5]
data[1:4] = [20, 30, 40]
print("slice-updated data:", data)


# ------------------------------------------------------------
# 5) Adding items
# ------------------------------------------------------------
items = [1, 2]

items.append(3)          # Add one item at end
items.extend([4, 5])     # Add multiple items
items.insert(1, 99)      # Insert at index 1

print("after add operations:", items)


# ------------------------------------------------------------
# 6) Removing items
# ------------------------------------------------------------
values = [10, 20, 20, 30, 40]

values.remove(20)        # Removes first matching value only
last_item = values.pop() # Removes and returns last item
del values[0]            # Deletes item at index 0

print("after remove/pop/del:", values)
print("popped item:", last_item)

# clear() removes all elements from list.
temp = [1, 2, 3]
temp.clear()
print("after clear:", temp)


# ------------------------------------------------------------
# 7) Useful operations
# ------------------------------------------------------------
arr = [3, 1, 4, 1, 5]

print("length len(arr):", len(arr))
print("is 4 in arr?:", 4 in arr)
print("count of 1:", arr.count(1))
print("index of 5:", arr.index(5))
print("min:", min(arr), "max:", max(arr), "sum:", sum(arr))


# ------------------------------------------------------------
# 8) Sorting and reversing
# ------------------------------------------------------------
scores = [50, 10, 70, 20]

scores.sort()  # Sort in ascending order (in-place)
print("sorted ascending:", scores)

scores.sort(reverse=True)  # Sort descending
print("sorted descending:", scores)

words = ["banana", "kiwi", "apple", "grape"]
words.sort(key=len)  # Sort by word length
print("words sorted by length:", words)

# reverse() changes original list order.
scores.reverse()
print("scores after reverse():", scores)


# ------------------------------------------------------------
# 9) Copying lists (important)
# ------------------------------------------------------------
original = [1, 2, 3]
alias = original         # Not a real copy (same object)
copied = original.copy() # Real shallow copy

alias[0] = 999
print("original after alias change:", original)  # changed
print("copied remains:", copied)                 # unchanged


# ------------------------------------------------------------
# 10) Nested lists
# ------------------------------------------------------------
# A list can contain other lists.
matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]

print("matrix:", matrix)
print("matrix[1]:", matrix[1])      # second row
print("matrix[1][2]:", matrix[1][2])  # value 6


# ------------------------------------------------------------
# 11) List comprehension
# ------------------------------------------------------------
# A compact way to build a list.
squares = [x * x for x in range(6)]
evens = [x for x in range(10) if x % 2 == 0]

print("squares:", squares)
print("evens:", evens)


# ------------------------------------------------------------
# 12) Common mistakes
# ------------------------------------------------------------
# a) IndexError: using invalid index (example: arr[100]).
# b) append vs extend:
#    append([7, 8]) -> adds list as ONE item.
#    extend([7, 8]) -> adds 7 and 8 as separate items.
# c) Modifying a list while iterating over the same list can skip items.
# d) Using list as a variable name is not recommended because it shadows
#    Python's built-in list type.


# ------------------------------------------------------------
# 13) Time complexity (basic)
# ------------------------------------------------------------
# Index access            : O(1)
# Append at end (average) : O(1)
# Insert/delete middle    : O(n)
# Membership test (x in L): O(n)
# Sorting                 : O(n log n)


print("\nDone: Python list notes with examples executed successfully.")