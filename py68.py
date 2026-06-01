"""
Positional and Keyword arguments — short examples and comments.
"""

# Positional arguments: order matters.
def divide(a, b):
	# a: numerator, b: denominator
	return a / b

print('positional ->', divide(10, 2))       # 5.0 (a=10, b=2)
print('positional swapped ->', divide(2, 10))  # 0.2 (a=2, b=10)

# Keyword arguments: specify parameter names, order does not matter.
print('keyword ->', divide(a=10, b=2))      # 5.0
print('keyword swapped ->', divide(b=2, a=10)) # 5.0 (same result)

# Mixing: positional arguments must come before keyword arguments.
def greet(greeting, name):
	return f"{greeting}, {name}"

print(greet('Hi', name='Bob'))  # valid: positional then keyword
# The following is invalid and would raise a SyntaxError if uncommented:
# greet(name='Bob', 'Hi')  # cannot have positional after keyword

# Short tip: use keywords for clarity when calling functions with many parameters.

