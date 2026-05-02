# F-STRINGS IN PYTHON
# F-strings = formatted string literals (Python 3.6+)
# Prefix string with 'f' or 'F' and use {} to embed expressions

# BASIC EXAMPLE
name = "Alice"
age = 30
print(f"{name} is {age} years old.")  # Output: Alice is 30 years old.

# YOU CAN PUT ANY EXPRESSION INSIDE {}
price = 49.99
quantity = 3
print(f"Total: ${price * quantity:.2f}")  # Output: Total: $149.97

# CALL FUNCTIONS INSIDE {}
print(f"Uppercase: {name.upper()}")  # Output: Uppercase: ALICE

# FORMAT NUMBERS
pi = 3.14159265
print(f"Pi to 2 decimals: {pi:.2f}")  # Output: Pi to 2 decimals: 3.14
print(f"Percentage: {0.25:.1%}")      # Output: Percentage: 25.0%

# MULTILINE F-STRING
message = f"""
Name: {name}
Age: {age}
Next year: {age + 1}
"""
print(message)

# DICTIONARY ACCESS
person = {"name": "Bob", "job": "engineer"}
print(f"{person['name']} works as an {person['job']}")

# DEBUGGING (Python 3.8+)
x = 42
print(f"{x=}")  # Output: x=42