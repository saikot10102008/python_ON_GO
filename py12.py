# =============================================================================
# LOGICAL OPERATORS IN PYTHON - SIMPLY EXPLAINED
# =============================================================================

# Logical operators are used to combine multiple conditions and make decisions
# They work with Boolean values (True/False)

# -----------------------------------------------------------------------------
# THE 3 LOGICAL OPERATORS:
# -----------------------------------------------------------------------------

# 1. and - ALL conditions must be True
# 2. or  - AT LEAST ONE condition must be True
# 3. not - REVERSES the condition (True becomes False, False becomes True)

# -----------------------------------------------------------------------------
# 1. AND OPERATOR (and)
# -----------------------------------------------------------------------------

print("=== 1. AND OPERATOR (and) ===")
print("Rule: ALL conditions must be True for the result to be True")
print("Think: 'Both must be true'")
print()

# Example 1: Simple and operator
has_ticket = True
has_id = True

print(f"has_ticket = {has_ticket}, has_id = {has_id}")
print(f"Can enter? has_ticket and has_id = {has_ticket and has_id}")  # True
print()

# Example 2: One condition is False
has_ticket = True
has_id = False

print(f"has_ticket = {has_ticket}, has_id = {has_id}")
print(f"Can enter? has_ticket and has_id = {has_ticket and has_id}")  # False
print()

# Example 3: Both conditions are False
has_ticket = False
has_id = False

print(f"has_ticket = {has_ticket}, has_id = {has_id}")
print(f"Can enter? has_ticket and has_id = {has_ticket and has_id}")  # False
print()

# -----------------------------------------------------------------------------
# 2. OR OPERATOR (or)
# -----------------------------------------------------------------------------

print("=== 2. OR OPERATOR (or) ===")
print("Rule: AT LEAST ONE condition must be True for the result to be True")
print("Think: 'Either one or both can be true'")
print()

# Example 1: Simple or operator
has_cash = True
has_card = False

print(f"has_cash = {has_cash}, has_card = {has_card}")
print(f"Can pay? has_cash or has_card = {has_cash or has_card}")  # True
print()

# Example 2: Both conditions are True
has_cash = True
has_card = True

print(f"has_cash = {has_cash}, has_card = {has_card}")
print(f"Can pay? has_cash or has_card = {has_cash or has_card}")  # True
print()

# Example 3: Both conditions are False
has_cash = False
has_card = False

print(f"has_cash = {has_cash}, has_card = {has_card}")
print(f"Can pay? has_cash or has_card = {has_cash or has_card}")  # False
print()

# -----------------------------------------------------------------------------
# 3. NOT OPERATOR (not)
# -----------------------------------------------------------------------------

print("=== 3. NOT OPERATOR (not) ===")
print("Rule: REVERSES the Boolean value")
print("Think: 'Opposite of what it is'")
print()

# Example 1: Simple not operator
is_raining = True

print(f"is_raining = {is_raining}")
print(f"Should we stay inside? is_raining = {is_raining}")
print(f"Should we go outside? not is_raining = {not is_raining}")  # False
print()

# Example 2: Not with False
is_weekend = False

print(f"is_weekend = {is_weekend}")
print(f"Go to work? not is_weekend = {not is_weekend}")  # True
print()

# -----------------------------------------------------------------------------
# REAL-LIFE EXAMPLES
# -----------------------------------------------------------------------------

print("=== REAL-LIFE EXAMPLES ===")

# Example 1: Age check for driving
age = 17
has_license = False

print(f"Age: {age}, Has license: {has_license}")
print(f"Can drive? age >= 18 and has_license = {age >= 18 and has_license}")
print()

# Example 2: Discount eligibility
is_student = True
is_senior = False
has_coupon = True

print(f"Student: {is_student}, Senior: {is_senior}, Has coupon: {has_coupon}")
print(
    f"Get discount? is_student or is_senior or has_coupon = {is_student or is_senior or has_coupon}"
)
print()

# Example 3: Secure login
username_correct = True
password_correct = False

print(f"Username correct: {username_correct}, Password correct: {password_correct}")
print(
    f"Login successful? username_correct and password_correct = {username_correct and password_correct}"
)
print()

# -----------------------------------------------------------------------------
# COMBINING LOGICAL OPERATORS
# -----------------------------------------------------------------------------

print("=== COMBINING OPERATORS ===")

# Example: Amusement park ride
height = 48  # inches
age = 12
has_parent = True

print(f"Height: {height} inches, Age: {age}, Has parent: {has_parent}")

# Rule: Can ride if (height >= 48) OR (age >= 13) OR (has_parent and age >= 10)
can_ride = (height >= 48) or (age >= 13) or (has_parent and age >= 10)
print(f"Can ride? {can_ride}")
print()

# -----------------------------------------------------------------------------
# TRUTH TABLES (HOW LOGICAL OPERATORS WORK)
# -----------------------------------------------------------------------------

print("=== TRUTH TABLES ===")

print("AND Truth Table:")
print("True  and True  =", True and True)  # True
print("True  and False =", True and False)  # False
print("False and True  =", False and True)  # False
print("False and False =", False and False)  # False
print()

print("OR Truth Table:")
print("True  or True  =", True or True)  # True
print("True  or False =", True or False)  # True
print("False or True  =", False or True)  # True
print("False or False =", False or False)  # False
print()

print("NOT Truth Table:")
print("not True  =", not True)  # False
print("not False =", not False)  # True
print()

# -----------------------------------------------------------------------------
# COMMON MISTAKES
# -----------------------------------------------------------------------------

print("=== COMMON MISTAKES ===")

# Mistake 1: Using & (bitwise AND) instead of 'and'
# Mistake 2: Using | (bitwise OR) instead of 'or'
# Mistake 3: Confusing = (assignment) with == (comparison)

# CORRECT:
x = 5
y = 10
print(f"x = {x}, y = {y}")
print(f"x > 0 and y > 0: {x > 0 and y > 0}")  # True
print()

# WRONG (but won't error, just different meaning):
print(f"x > 0 & y > 0: {x > 0 & y > 0}")  # Uses bitwise AND - avoid!
print()

# -----------------------------------------------------------------------------
# PRACTICE EXERCISE
# -----------------------------------------------------------------------------

print("=== PRACTICE EXERCISE ===")

# Fill in the blanks with and, or, not
weather = "sunny"
temperature = 25
have_umbrella = False

print(
    f"Weather: {weather}, Temperature: {temperature}°C, Have umbrella: {have_umbrella}"
)
print()

# Question 1: Good day for picnic?
# Picnic is good if: weather is sunny AND temperature is above 20
good_for_picnic = (weather == "sunny") and (temperature > 20)
print(f"Good for picnic? {good_for_picnic}")
print()

# Question 2: Should take umbrella?
# Take umbrella if: weather is rainy OR we don't have one
should_take_umbrella = (weather == "rainy") or (not have_umbrella)
print(f"Should take umbrella? {should_take_umbrella}")
print()

# -----------------------------------------------------------------------------
# QUICK REFERENCE
# -----------------------------------------------------------------------------

print("=== QUICK REFERENCE ===")
print("Operator | Meaning                      | Example              | Result")
print("---------|------------------------------|----------------------|-------")
print("and      | Both must be True            | True and False       | False")
print("or       | At least one must be True    | True or False        | True ")
print("not      | Reverses the value           | not True             | False")
print()

print("=" * 60)
print("Remember:")
print("1. and -> ALL conditions must be True")
print("2. or  -> AT LEAST ONE condition must be True")
print("3. not -> REVERSE the condition")
print("=" * 60)
