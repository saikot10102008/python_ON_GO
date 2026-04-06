# ============================================
# 1. BASIC INPUT AND DEFAULT INPUT TYPE
# ============================================

# Input always takes input as a STRING by default
name = input("Enter your name: ")
print("You entered:", name)
print("Type of input:", type(name))  # Always <class 'str'>

# Even numbers are taken as strings
age = input("Enter your age: ")
print("Age is stored as:", type(age))  # Still string type

# To use age as number, we would need to convert it (but not doing here as per rules)


# ============================================
# 2. CHANGING INPUT TYPE (using type conversion)
# ============================================

# Input is string by default, but we can convert it
number_str = input("Enter a number: ")
print("Before conversion:", type(number_str))

# Converting string input to integer
number_int = int(number_str)  # Changing type from str to int
print("After conversion to int:", type(number_int))

# Converting to float
number_float = float(number_str)
print("After conversion to float:", type(number_float))


# ============================================
# 3. F-STRING (Formatted String)
# ============================================

# F-strings allow embedding variables directly in strings
name = "Alice"
age = 25
city = "New York"

# Using f-string with f prefix
print(f"Hello, my name is {name} and I am {age} years old from {city}")

# Can also do calculations inside f-string
print(f"Next year I will be {age + 1} years old")

# F-string with input
color = input("Enter your favorite color: ")
print(f"Your favorite color is {color}")


# ============================================
# 4. RAW STRING (r-string)
# ============================================

# Raw strings treat backslashes as literal characters, not escape sequences
# Normal string with escape sequence
normal_path = "C:\\Users\\Name\\Documents"
print("Normal string:", normal_path)  # Double backslash needed

# Raw string - backslashes are treated as normal characters
raw_path = r"C:\Users\Name\Documents"
print("Raw string:", raw_path)  # Prints with single backslashes

# Another example - newline escape
normal_text = "Hello\nWorld"
print("Normal with newline:")
print(normal_text)

raw_text = r"Hello\nWorld"
print("Raw string (\\n is literal):")
print(raw_text)


# ============================================
# 5. F-STRING AND RAW STRING TOGETHER
# ============================================

# You can combine f and r (order doesn't matter: rf or fr)
name = "Bob"
file_path = r"C:\Users\Bob\Desktop"

# Using fr-string (f and r together)
print(fr"Hello {name}, your file is at: {file_path}")

# Also works as rf
print(rf"User {name} has path: {file_path}")

# Practical example with escape sequences
special_char = "TAB\tHERE"
print(fr"Raw+f shows: {special_char} literally")  # \t shows as \t not as tab


# ============================================
# 6. RAW STRING MULTILINE
# ============================================

# Using triple quotes with raw string
multiline_raw = r"""
This is a raw multiline string.
Backslashes are literal: C:\Users\Name
Newlines \n are just text here.
Tabs \t don't actually tab.
"""
print("Raw multiline string:")
print(multiline_raw)

# Another example - showing Windows path with newlines
raw_multiline_path = r"""
Common Windows paths:
C:\Program Files\App
D:\Backup\Documents
E:\Media\Videos\new folder  (note: \n is literal)
"""
print(raw_multiline_path)


# ============================================
# 7. F AND RAW STRING TOGETHER MULTILINE
# ============================================

# Combining f-string and raw string with multiline
user = "Charlie"
folder = "Projects"
filename = "data.txt"

# Using fr with triple quotes
multiline_fr = fr"""
User: {user}
File location: C:\Users\{user}\Documents\{folder}
Raw path keeps backslashes: C:\Folder\Subfolder\nested (note \n is literal)
Filename: {filename}
"""
print("F and Raw combined multiline:")
print(multiline_fr)

# Another example with calculations
quantity = 5
price = 19.99
multiline_order = fr"""
Order Summary for {user}:
Quantity: {quantity}
Price per item: ${price}
Total: ${quantity * price}
Save path: D:\Orders\{user}\invoice_{quantity}_items.txt (raw path)
Note: \t and \n are shown as text, not as special characters
"""
print(multiline_order)


# ============================================
# DEMONSTRATION WITH USER INPUT
# ============================================

# Taking input and using all concepts together
print("\n" + "="*50)
print("FINAL DEMONSTRATION WITH YOUR INPUT")
print("="*50)

user_name = input("Enter your name: ")
user_city = input("Enter your city: ")
user_path = input("Enter a file path (like C:\\Users\\Name): ")

# Using f-string for normal output
print(f"\n--- Hello {user_name} from {user_city} ---")

# Using raw string for path display
print(rf"Your entered path (raw): {user_path}")

# Using multiline fr-string
final_output = fr"""
=== COMPLETE INFO ===
Name: {user_name}
City: {user_city}
Path: {user_path}
Note in raw string: \n \t \r are all literal characters
"""
print(final_output)

print("Program completed successfully!")