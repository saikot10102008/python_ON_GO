"""
if, elif, and else in Python

Use:
- if: run code when a condition is True
- elif: check another condition if the previous one was False
- else: run code when none of the above conditions are True
"""

# Example value to test
marks = 72

# if checks the first condition
if marks >= 90:
	print("Grade: A")

# elif checks the next condition only if the if condition was False
elif marks >= 75:
	print("Grade: B")

# another elif for a different range
elif marks >= 60:
	print("Grade: C")

# else runs when none of the conditions above are True
else:
	print("Grade: D")

# You can use if/elif/else to choose between multiple paths in a program.
# Python uses indentation to show which lines belong to each block.
