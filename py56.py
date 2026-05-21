"""
Exception handling in Python

This file is written as a beginner-friendly note.
It explains what exceptions are, why they matter, and how to handle them
with simple examples.

Rules for this note:
- no file handling examples
- no classes or OOP
- no advanced Python features
- only simple functions, comments, and basic control flow
"""


print("Exception Handling in Python")
print("=" * 35)


# ------------------------------------------------------------
# 1. What is an exception?
# ------------------------------------------------------------
# An exception is an error that happens while a program is running.
# If we do not handle it, the program stops immediately.
#
# Example:
#   10 / 0
# This causes a ZeroDivisionError because division by zero is not allowed.

print("\n1) What is an exception?")
print("An exception is a runtime error that can stop your program.")


# ------------------------------------------------------------
# 2. Why exception handling is useful
# ------------------------------------------------------------
# Exception handling helps us:
# - stop the program from crashing suddenly
# - show a helpful message to the user
# - recover from a problem and continue running

print("\n2) Why exception handling is useful")
print("It helps the program stay alive when something goes wrong.")


# ------------------------------------------------------------
# 3. The basic try and except structure
# ------------------------------------------------------------
# try:
#     code that may fail
# except SomeError:
#     code that runs if that error happens
#
# We put risky code inside try.
# We put the handling code inside except.


print("\n3) Basic try and except")

try:
	number = 10 / 2
	print("10 / 2 =", number)
except ZeroDivisionError:
	# This block will not run here because the division is safe.
	print("You cannot divide by zero.")


# Example with a real failure
try:
	number = 10 / 0
	print("This line will not run.")
except ZeroDivisionError:
	print("Handled: You cannot divide by zero.")


# ------------------------------------------------------------
# 4. Catching different exceptions
# ------------------------------------------------------------
# Different problems raise different exception types.
# We can use different except blocks for different errors.

print("\n4) Catching different exceptions")

text = "hello"

try:
	# This will fail because text cannot be converted to an integer.
	value = int(text)
	print("Converted value:", value)
except ValueError:
	print("Handled: The text could not be converted to an integer.")


try:
	# This will fail because the list index is out of range.
	numbers = [1, 2, 3]
	print(numbers[5])
except IndexError:
	print("Handled: That list index does not exist.")


# ------------------------------------------------------------
# 5. Using 'as' to capture the error message
# ------------------------------------------------------------
# 'as e' stores the exception object in a variable.
# This lets us print the exact error message.

print("\n5) Capturing the error message")

try:
	result = 5 / 0
except ZeroDivisionError as error_message:
	print("Handled error:", error_message)


# ------------------------------------------------------------
# 6. Handling multiple possible errors
# ------------------------------------------------------------
# Sometimes more than one thing can go wrong.
# We can write multiple except blocks.

print("\n6) Multiple possible errors")

sample_text = "25"

try:
	# int(sample_text) is okay here, but division by zero would fail if
	# the denominator were 0.
	converted_number = int(sample_text)
	answer = converted_number / 5
	print("Answer:", answer)
except ValueError:
	print("Handled: The text is not a valid integer.")
except ZeroDivisionError:
	print("Handled: Division by zero happened.")


# ------------------------------------------------------------
# 7. A general except block
# ------------------------------------------------------------
# A bare except is not a good habit because it can hide real problems.
# Still, it is useful to know that it exists.
# It should be used carefully.

print("\n7) General except block")

try:
	value = int("100")
	print("Converted value:", value)
except Exception:
	print("Something went wrong.")


# Better practice is to catch a specific error whenever possible.


# ------------------------------------------------------------
# 8. The else block
# ------------------------------------------------------------
# else runs only when no exception happens.
# It is useful when you want to separate successful code
# from error-handling code.

print("\n8) The else block")

try:
	number = int("42")
except ValueError:
	print("Could not convert the text to a number.")
else:
	print("Conversion worked, number =", number)


# Another example where else does not run because an error occurs.
try:
	number = int("not a number")
except ValueError:
	print("Handled: conversion failed.")
else:
	print("This will not print.")


# ------------------------------------------------------------
# 9. The finally block
# ------------------------------------------------------------
# finally runs no matter what happens.
# It is used for cleanup or final messages.
# In this beginner note, we use it to show that it always runs.

print("\n9) The finally block")

try:
	result = 8 / 2
	print("Result:", result)
except ZeroDivisionError:
	print("Handled: division by zero.")
finally:
	print("This message always runs.")


try:
	result = 8 / 0
	print("Result:", result)
except ZeroDivisionError:
	print("Handled: division by zero.")
finally:
	print("This message still runs even after the error.")


# ------------------------------------------------------------
# 10. Raising an exception yourself
# ------------------------------------------------------------
# Sometimes you want Python to stop and show an error on purpose.
# You can use raise.
#
# Example: if a number is negative, we may want to reject it.

print("\n10) Raising an exception yourself")

age = 18

try:
	if age < 0:
		raise ValueError("Age cannot be negative.")
	print("Age is valid:", age)
except ValueError as error_message:
	print("Handled:", error_message)


try:
	age = -5
	if age < 0:
		raise ValueError("Age cannot be negative.")
	print("Age is valid:", age)
except ValueError as error_message:
	print("Handled:", error_message)


# ------------------------------------------------------------
# 11. Simple helper functions with exception handling
# ------------------------------------------------------------
# Functions are still beginner-friendly, so we can use them.
# They help us group logic into small reusable pieces.

print("\n11) Simple helper functions")


def safe_divide(a, b):
	# This function tries to divide two numbers safely.
	try:
		return a / b
	except ZeroDivisionError:
		return "Cannot divide by zero"


def safe_int(text_value):
	# This function converts text into an integer.
	try:
		return int(text_value)
	except ValueError:
		return "Invalid integer text"


print("safe_divide(12, 3) ->", safe_divide(12, 3))
print("safe_divide(12, 0) ->", safe_divide(12, 0))
print("safe_int('56') ->", safe_int("56"))
print("safe_int('abc') ->", safe_int("abc"))


# ------------------------------------------------------------
# 12. Common beginner mistakes
# ------------------------------------------------------------
# Mistake 1: catching the wrong exception type
# Mistake 2: writing risky code outside try
# Mistake 3: using a very broad except when a specific one is better
#
# Example of a safe pattern:

print("\n12) Common beginner mistakes and safe patterns")

try:
	first_number = int("10")
	second_number = int("0")
	print(first_number / second_number)
except ValueError:
	print("Handled: one of the values was not a valid number.")
except ZeroDivisionError:
	print("Handled: division by zero.")
else:
	print("No errors happened in the try block.")
finally:
	print("This runs at the end.")


# ------------------------------------------------------------
# 13. Easy summary
# ------------------------------------------------------------
# try: run code that might fail
# except: handle the failure
# else: run if no error happened
# finally: run no matter what
# raise: create an error on purpose

print("\n13) Summary")
print("try -> risky code")
print("except -> handle the error")
print("else -> runs when there is no error")
print("finally -> always runs")
print("raise -> create an error intentionally")


print("\nEnd of exception handling note.")
