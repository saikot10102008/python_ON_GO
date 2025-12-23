# ASSIGNMENT OPERATORS
# ====================
# Used to assign values to variables

# 1. = (Simple Assignment)
# Assigns value on right to variable on left
x = 10
print(f"x = 10 → x = {x}")

# 2. += (Add AND Assignment)
# Adds right value to left variable, then assigns result
x += 5  # Same as: x = x + 5
print(f"x += 5 → x = {x}")

# 3. -= (Subtract AND Assignment)
# Subtracts right value from left variable, then assigns result
x -= 3  # Same as: x = x - 3
print(f"x -= 3 → x = {x}")

# 4. *= (Multiply AND Assignment)
# Multiplies left variable by right value, then assigns result
x *= 2  # Same as: x = x * 2
print(f"x *= 2 → x = {x}")

# 5. /= (Divide AND Assignment)
# Divides left variable by right value, then assigns result (float)
x /= 4  # Same as: x = x / 4
print(f"x /= 4 → x = {x}")

# 6. //= (Floor Divide AND Assignment)
# Divides and floors result, then assigns (integer)
x //= 2  # Same as: x = x // 2
print(f"x //= 2 → x = {x}")

# 7. %= (Modulus AND Assignment)
# Takes modulus, then assigns remainder
x %= 3  # Same as: x = x % 3
print(f"x %= 3 → x = {x}")

# 8. **= (Exponent AND Assignment)
# Raises to power, then assigns result
x **= 2  # Same as: x = x ** 2
print(f"x **= 2 → x = {x}")

# Quick Examples:
a = 100
a += 20   # a = 120
a -= 30   # a = 90
a *= 2    # a = 180
a /= 3    # a = 60.0
a //= 7   # a = 8.0
a %= 5    # a = 3.0
a **= 3   # a = 27.0