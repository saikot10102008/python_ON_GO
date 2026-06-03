import math  # Required for pi, sqrt, ceil, floor, etc.

print("=== Basic Arithmetic Operators ===\n")

# 1. Basic operators
friends = 0
friends = friends + 1          # Addition
print("friends + 1 =", friends)

friends = friends - 2          # Subtraction
print("friends - 2 =", friends)

friends = friends * 5          # Multiplication
print("friends * 5 =", friends)

friends = friends / 2          # Division (returns float)
print("friends / 2 =", friends)

friends = friends ** 2         # Exponentiation (power)
print("friends ** 2 =", friends)

friends = 10
remainder = friends % 3        # Modulus (remainder)
print("10 % 3 =", remainder)   # Useful for even/odd checks

# Shorthand assignment operators
friends = 10
friends += 1   # friends = friends + 1
friends -= 2   # friends = friends - 2
friends *= 3   # friends = friends * 3
friends /= 2   # friends = friends / 2
friends **= 2  # friends = friends ** 2
print("Final friends value:", friends)


print("\n=== Built-in Math Functions ===\n")

x = 3.14
y = 4
z = 5

print("round(3.14)   =", round(x))           # Round to nearest integer
print("abs(-3.14)    =", abs(-x))             # Absolute value
print("pow(4, 2)     =", pow(y, 2))           # Power (same as **)
print("max(3.14,4,5) =", max(x, y, z))        # Maximum value
print("min(3.14,4,5) =", min(x, y, z))        # Minimum value


print("\n=== Math Module (import math) ===\n")

print("math.pi      =", math.pi)
print("math.e       =", math.e)

print("math.sqrt(9) =", math.sqrt(9))         # Square root
print("math.ceil(9.1)  =", math.ceil(9.1))    # Round UP
print("math.floor(9.9) =", math.floor(9.9))   # Round DOWN


print("\n=== Exercise 1: Circumference of a Circle ===\n")
# Formula: C = 2 * π * r

radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)} cm")


print("\n=== Exercise 2: Area of a Circle ===\n")
# Formula: A = π * r²

radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius, 2)        # or radius ** 2
print(f"The area of the circle is: {round(area, 2)} cm²")


print("\n=== Exercise 3: Hypotenuse of Right Triangle ===\n")
# Formula: c = √(a² + b²)

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))   # or math.sqrt(a**2 + b**2)
print(f"Side C (hypotenuse) = {round(c, 2)}")


print("\n=== All done! Math in Python really is easy! ===")