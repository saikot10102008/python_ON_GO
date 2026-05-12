# tuples

tuple = (1,22,33,33,33,3,4)

# method 1

a = tuple.count(33)

# method 2

b = tuple.index(22)
c = tuple.index(33)

print(f"tuple.count(33) = {a} \ntuple.index(22) = {b} \ntuple.index(33) = {c}")

# TUPLE UNPACKING - Assigns elements from a tuple to multiple variables in one statement

# Basic unpacking: number of variables must match number of elements
x, y, z = (10, 20, 30)
print(f"\nBasic unpacking: x={x}, y={y}, z={z}")

# Works without parentheses (tuples can be implicit)
a, b = 100, 200
print(f"Implicit tuple: a={a}, b={b}")

# Unpacking from a list (works with any iterable)
p, q, r = [1, 2, 3]
print(f"From list: p={p}, q={q}, r={r}")

# Swapping variables using unpacking
num1, num2 = 5, 10
num1, num2 = num2, num1  # Swapped in one line
print(f"After swap: num1={num1}, num2={num2}")

# Unpacking with * to capture multiple elements
first, *middle, last = (1, 2, 3, 4, 5)
print(f"With *: first={first}, middle={middle}, last={last}")

# Ignoring values with underscore
name, _, age = ("Alice", "Engineer", 30)
print(f"Ignored middle value: name={name}, age={age}")

# Unpacking function returns
def get_coordinates():
    return (5, 10)
x_coord, y_coord = get_coordinates()
print(f"From function return: x={x_coord}, y={y_coord}")

# IMPORTANT: Parentheses vs Comma in tuples
# (1) creates an INTEGER - parentheses are just for grouping, NOT a tuple
a = (1)
print(f"\na = (1): type is {type(a)}, value = {a}")  # <class 'int'>

# (1,) creates a TUPLE with one element - the COMMA is what makes it a tuple
b = (1,)
print(f"a = (1,): type is {type(b)}, value = {b}")  # <class 'tuple'>

# More examples
c = (5)
d = (5,)
print(f"\n(5) is {type(c)} = {c}")    # int
print(f"(5,) is {type(d)} = {d}")   # tuple

# This is why you need comma for single-element tuples
single_tuple = (42,)  # Always use comma for single-element tuples!
print(f"\nSingle element tuple: {single_tuple}, type: {type(single_tuple)}")


