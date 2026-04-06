# ========================================================
# f-STRING + RAW STRING + INPUT() + TYPE CONVERSION
# ========================================================

print("=== f-STRING + RAW STRING + INPUT() GUIDE ===\n")

# ========================================================
# 1. f-STRING (Formatted String Literal)
# ========================================================
# Introduced in Python 3.6
# Fastest and most readable way to embed variables/expressions inside strings.
# Syntax: f"some text {variable} more text"   or   F"..."

print("=== 1. f-STRING ===")

name = "Sakhwat"
age = 25
height = 5.9
score = 92.75

# Basic usage
print(f"My name is {name} and I am {age} years old.")

# You can put ANY Python expression inside {}
print(f"Next year I will be {age + 1} years old.")
print(f"Height in cm: {height * 30.48:.2f}")          # :.2f = 2 decimal places
print(f"Score: {score}% → Grade: {'A' if score >= 90 else 'B'}")

# Multi-line f-string
message = f"""Hello {name}!
You are {age} years old.
Your score is {score:.1f}"""
print(message)

# Advantages of f-strings:
# - Faster than .format() and % formatting
# - Cleaner syntax
# - Supports all formatting options

# ========================================================
# 2. RAW STRING (r-string)
# ========================================================
# Prefix: r"..." or R"..."
# Treats backslashes (\) as literal characters instead of escape sequences.
# Extremely useful for:
#   - Regular expressions
#   - File paths on Windows
#   - LaTeX, JSON, etc.

print("\n=== 2. RAW STRING ===")

# Normal string vs Raw string
normal = "C:\new_folder\test.py"      # \n becomes newline!
print("Normal string  :", normal)

raw = r"C:\new_folder\test.py"        # backslashes stay as \
print("Raw string     :", raw)

# Real-world examples:

# 1. File path (Windows)
path = r"C:\Users\Sakhwat\Documents\file.txt"
print("Windows path   :", path)

# 2. Regular Expression (very common use)
regex = r"\d{3}-\d{2}-\d{4}"          # Social Security Number pattern
print("Regex pattern  :", regex)

# 3. Multi-line raw string
multi_raw = r"""Line1
C:\path\to\file
Line3 with \n and \t"""
print("Multi-line raw:\n", multi_raw)

# Note:
# You can combine raw + f-string: rf"..." or fr"..."
print(rf"Raw + f-string: Path = C:\Users\{name}\file.txt")

# ========================================================
# 3. INPUT() FUNCTION
# ========================================================
# Built-in function to read input from the user (console).
# Always pauses the program and waits for Enter key.

print("\n=== 3. INPUT() ===")
print("Demonstrating input()... (uncomment the lines below to test)")

# Example 1: Basic input
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# Example 2: Input with prompt
# age_input = input("How old are you? ")
# print(f"You entered: {age_input}")

# ========================================================
# 4. DEFAULT DATA TYPE OF INPUT()
# ========================================================
# VERY IMPORTANT:
# input() ALWAYS returns a STRING (str), even if you type a number!

print("\n=== 4. DEFAULT DATA TYPE OF input() ===")

# Simulated input (we can't run real input in this explanation file,
# but this is exactly what happens):

simulated_input = "25"          # ← this is what input() actually gives you
print(f"What user typed     : {simulated_input}")
print(f"Type of input()     : {type(simulated_input)}")   # <class 'str'>

# Common mistake:
# age = input("Age: ")          # age is str, not int!
# print(age + 5)                # This will give TypeError!

# ========================================================
# 5. CHANGING DATA TYPE OF INPUT (Type Conversion)
# ========================================================
# You MUST convert the string returned by input() to the type you need.
# This is where explicit type conversion (from previous file) is used.

print("\n=== 5. CHANGING DATA TYPE OF INPUT ===")

# Correct way - convert immediately after input
# age_str = input("Enter your age: ")
# age = int(age_str)                    # convert str → int

# Even shorter (most common in real code):
# age = int(input("Enter your age: "))

# Examples of conversion after input:

# Integer
# num = int(input("Enter a whole number: "))

# Float
# price = float(input("Enter price: "))

# Boolean (a bit tricky)
# is_student = input("Are you a student? (yes/no): ").lower() == "yes"

print("Example conversions (using simulated input):")

# Simulate user typing "2026"
year = int("2026")
print(f"str '2026' → int  : {year} (type: {type(year)})")

# Simulate user typing "99.99"
price = float("99.99")
print(f"str '99.99' → float: {price} (type: {type(price)})")

# Simulate user typing "Python"
language = "Python"
print(f"str remains str   : {language} (type: {type(language)})")

# ========================================================
# 6. COMMON PITFALLS & BEST PRACTICES
# ========================================================
print("\n=== 6. PITFALLS & BEST PRACTICES ===")

# Pitfall 1: Forgetting to convert input()
# age = input("Age: ")
# print(age + 10)          # TypeError: can only concatenate str

# Pitfall 2: Invalid conversion (user types wrong thing)
# age = int(input("Age: "))   # if user types "abc" → ValueError

# Best Practice: Always use try-except for real programs
def safe_input(prompt, data_type=int):
    while True:
        try:
            value = data_type(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please try again.")

# Example usage:
# age = safe_input("Enter your age: ", int)

# Best Practice: Combine f-string + input
# name = input("Name: ")
# print(f"Welcome, {name.title()}!")

# ========================================================
# SUMMARY TABLE (in comments)
# ========================================================
# Feature              | Syntax                | Returns    | Use Case
# -------------------------------------------------------------------
# f-string             | f"{}"                 | str        | Modern formatting
# Raw string           | r"..."                | str        | Paths, regex
# input()              | input("prompt")       | ALWAYS str | User input
# Convert input        | int(input()), float() | int/float  | Numbers from user
# Raw + f-string       | rf"..."               | str        | Dynamic paths/regex

print("\n=== END OF GUIDE ===")
print("You now know f-strings, raw strings, input(), and how to handle its data type!")
print("Run this file again and experiment with the commented input() examples.")