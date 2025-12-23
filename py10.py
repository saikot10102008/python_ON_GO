# Arithmetic Operators
x = 10
y = 20

print("x =", x, "y =", y)
print()

# 1. ADDITION (+)
print(f"{x} + {y} = {x + y}")  # 10 + 20 = 30

# 2. SUBTRACTION (-)
print(f"{x} - {y} = {x - y}")  # 10 - 20 = -10

# 3. MULTIPLICATION (*)
print(f"{x} * {y} = {x * y}")  # 10 * 20 = 200

# 4. REGULAR DIVISION (/)
# Gives result with decimal (float)
print(f"{x} / {y} = {x / y}")  # 10 ÷ 20 = 0.5

# 5. FLOOR DIVISION (//)
# Gives whole number result (rounds down)
print(f"{x} // {y} = {x // y}")  # 10 ÷ 20 = 0 (0.5 rounds down to 0)

# Example with floor division:
print(f"15 // 4 = {15 // 4}")  # 15 ÷ 4 = 3.75, floor = 3
print(f"17 // 5 = {17 // 5}")  # 17 ÷ 5 = 3.4, floor = 3
print(f"-17 // 5 = {-17 // 5}")  # -3.4 rounds DOWN to -4 (careful!)

# 6. MODULUS (%)
# Gives the REMAINDER after division
print(f"{x} % {y} = {x % y}")  # 10 ÷ 20 = 0 remainder 10

# Example with modulus:
print(f"17 % 5 = {17 % 5}")  # 17 ÷ 5 = 3 remainder 2
print(f"10 % 3 = {10 % 3}")  # 10 ÷ 3 = 3 remainder 1
print(f"20 % 4 = {20 % 4}")  # 20 ÷ 4 = 5 remainder 0

# 7. EXPONENT (**)
# Power/Exponent operator (missing in your screenshot)
print(f"{x} ** 2 = {x ** 2}")  # 10² = 100
print(f"{y} ** 3 = {y ** 3}")  # 20³ = 8000