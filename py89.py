# Match-Case Statements in Python
# Introduced in Python 3.10+
# Match-case is Python's version of a switch statement.
# It provides a clean, readable way to compare a value against multiple patterns.
# Much better than long chains of if-elif-else statements.

# --------------------
# BASIC SYNTAX
# --------------------
# match subject:
#     case pattern1:
#         # code
#     case pattern2:
#         # code
#     case _ :          # wildcard (default case)
#         # code

def get_day_name(day_number):
    """Return day name from number 1-7"""
    match day_number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day number"


print("Day 3:", get_day_name(3))
print("Day 8:", get_day_name(8))

# --------------------
# MATCHING WITH STRINGS
# --------------------
def get_status(code):
    match code:
        case "200":
            return "OK"
        case "404":
            return "Not Found"
        case "500":
            return "Internal Server Error"
        case _:
            return "Unknown status code"


print("Status 200:", get_status("200"))
print("Status 999:", get_status("999"))

# --------------------
# COMBINING MULTIPLE VALUES IN ONE CASE
# --------------------
def is_weekend(day):
    match day.lower():
        case "saturday" | "sunday":   # | means OR
            return True
        case _:
            return False


print("Is Saturday weekend?", is_weekend("Saturday"))
print("Is Monday weekend?", is_weekend("Monday"))

# --------------------
# MATCHING WITH LISTS / TUPLES
# --------------------
def process_command(command):
    match command:
        case ["quit"] | ["exit"]:
            return "Goodbye!"
        case ["hello"] | ["hi"]:
            return "Hello there!"
        case ["add", x, y]:          # capture values
            return f"Sum = {int(x) + int(y)}"
        case _:
            return "Command not recognized"


print(process_command(["add", "5", "10"]))
print(process_command(["quit"]))

# --------------------
# GUARD CONDITIONS (if clause)
# --------------------
def classify_number(n):
    match n:
        case x if x > 0:
            return "Positive"
        case x if x < 0:
            return "Negative"
        case 0:
            return "Zero"
        case _:
            return "Not a number"


print("Classify 42:", classify_number(42))
print("Classify -7:", classify_number(-7))

# --------------------
# MATCHING DICTIONARIES / OBJECTS
# --------------------
def handle_event(event):
    match event:
        case {"type": "click", "button": "left"}:
            return "Left click detected"
        case {"type": "click", "button": "right"}:
            return "Right click detected"
        case {"type": "key", "key": key}:
            return f"Key pressed: {key}"
        case _:
            return "Unknown event"


print(handle_event({"type": "click", "button": "left"}))

# --------------------
# ADVANCED: MATCHING CLASSES / DATA CLASSES
# --------------------
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

def describe_point(point):
    match point:
        case Point(0, 0):
            return "Origin"
        case Point(0, y):
            return f"On the Y-axis at {y}"
        case Point(x, 0):
            return f"On the X-axis at {x}"
        case Point(x, y):
            return f"Point at ({x}, {y})"
        case _:
            return "Not a point"


print(describe_point(Point(3, 4)))
print(describe_point(Point(0, 5)))

# --------------------
# BEST PRACTICES & NOTES
# --------------------

# 1. The wildcard '_' catches anything not matched before it.
# 2. Cases are evaluated from top to bottom.
# 3. Match-case supports powerful pattern matching (literals, variables, sequences, mappings, classes).
# 4. You can capture values using variable names in patterns.
# 5. Use | to match multiple patterns in one case.
# 6. Add guard conditions with 'if' for extra logic.
# 7. Much cleaner than many elif statements for multiple conditions.

# Example of replacing if-elif chain:
def old_way(status):
    if status == 200:
        return "OK"
    elif status == 404:
        return "Not Found"
    else:
        return "Other"

# vs match-case (cleaner)

# Summary:
# - match-case is structural pattern matching
# - Very readable for multiple discrete values or complex patterns
# - Available in Python 3.10 and above
# - Great replacement for long switch-like logic