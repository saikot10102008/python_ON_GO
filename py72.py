# =====================================================
# CONDITIONAL EXPRESSIONS IN PYTHON
# =====================================================

print("=== Conditional Expressions (Ternary Operator) ===\n")

# A conditional expression is a one-line shortcut for if-else statements
# Syntax:   value_if_true if condition else value_if_false

# Example 1: Basic conditional expression
age = 25
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age} → Status: {status}")

age = 16
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age} → Status: {status}")


print("\n=== Real-world Examples ===\n")

# Example 2: Voting eligibility
age = int(input("Enter your age: "))
message = "You are eligible to vote!" if age >= 18 else "You are not eligible to vote yet."
print(message)


# Example 3: Even or Odd
number = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print(f"The number {number} is {result}.")


# Example 4: Discount based on purchase amount
amount = float(input("Enter purchase amount: $"))
discount = 0.2 if amount >= 100 else 0.1
final_price = amount * (1 - discount)
print(f"Discount applied: {discount*100}%")
print(f"Final price: ${final_price:.2f}")


print("\n=== Nested Conditional Expressions ===\n")

# You can nest them, but be careful with readability
score = int(input("Enter your exam score (0-100): "))

grade = ("A" if score >= 90 else
         "B" if score >= 80 else
         "C" if score >= 70 else
         "D" if score >= 60 else "F")

print(f"Your grade is: {grade}")


print("\n=== Comparing with Traditional if-else ===\n")

# Traditional way (multiple lines)
temperature = int(input("Enter temperature in °C: "))

if temperature > 30:
    weather = "Hot"
elif temperature > 20:
    weather = "Warm"
else:
    weather = "Cold"

print(f"Traditional if-else: It is {weather}")

# One-line conditional expression version
weather2 = "Hot" if temperature > 30 else "Warm" if temperature > 20 else "Cold"
print(f"Conditional expression: It is {weather2}")


print("\n=== Key Points ===\n")
print("• Conditional expressions are also called Ternary Operators")
print("• Syntax:  X if condition else Y")
print("• Great for simple if-else assignments or returning values")
print("• Makes code more concise")
print("• Can become hard to read if overused or nested too deeply")
print("• Best used for simple decisions")


print("\n=== All done! Conditional expressions are easy! ===")