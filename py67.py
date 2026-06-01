# Default argument: a parameter that has a value used when the caller omits it.

def greet(name="Guest"):
	# If the caller does not provide `name`, the default "Guest" is used.
	print('Hello,', name)

greet()          # prints: Hello, Guest
greet('Alice')   # prints: Hello, Alice

def add(a, b=10):
	# `b` defaults to 10 when not provided by the caller.
	return a + b

print(add(5))    # prints: 15 (uses default b=10)
print(add(5, 3)) # prints: 8  (overrides default with 3)

