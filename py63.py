"""
py63.py — concise list comprehension examples

Each example shows a short, real use case with a one-line
explanation in a comment and a printed result.
No advanced concepts are used.
"""

# 1) Basic mapping: squares of 0..4
# For each x in range(5), compute x*x and collect results.
squares = [x * x for x in range(5)]
print('squares ->', squares)  # [0, 1, 4, 9, 16]

# 2) Filtering: only even numbers from 0..9
# The `if` after the loop keeps items that match the condition.
evens = [x for x in range(10) if x % 2 == 0]
print('evens ->', evens)  # [0, 2, 4, 6, 8]

# 3) Transform strings: convert words to uppercase
words = ['apple', 'banana', 'cherry']
upper_words = [w.upper() for w in words]
print('upper_words ->', upper_words)  # ['APPLE', 'BANANA', 'CHERRY']

# 4) Nested loops: list of pairs (x, y)
# This is the same as a double for-loop but in one line.
pairs = [(x, y) for x in range(3) for y in range(2)]
print('pairs ->', pairs)  # [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

# 5) Flatten a 2D list (matrix) into a single list
matrix = [[1, 2], [3, 4], [5]]
flattened = [n for row in matrix for n in row]
print('flattened ->', flattened)  # [1, 2, 3, 4, 5]

# 6) Conditional expression inside comprehension
# Choose one of two values for each item.
labels = ['even' if x % 2 == 0 else 'odd' for x in range(6)]
print('labels ->', labels)  # ['even', 'odd', 'even', 'odd', 'even', 'odd']

# Short tip: prefer list comprehensions for short, clear transformations.
# If the code needs many steps or is hard to read, use a for-loop instead.


# check MD/list_comp.md