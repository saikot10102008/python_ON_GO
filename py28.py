# ===== isdigit() and isalpha() Methods =====

# isdigit() method:
# - Checks if ALL characters in a string are digits (0-9)
# - Returns True if all are digits, False otherwise
# - Returns False for empty strings

text1 = "12345"
print(f"'{text1}'.isdigit() = {text1.isdigit()}")  # True

text2 = "123abc"
print(f"'{text2}'.isdigit() = {text2.isdigit()}")  # False

text3 = "hello"
print(f"'{text3}'.isdigit() = {text3.isdigit()}")  # False

# isalpha() method:
# - Checks if ALL characters in a string are alphabetic (a-z, A-Z)
# - Returns True if all are letters, False otherwise
# - Returns False for empty strings
# - Does NOT include digits or special characters

text4 = "hello"
print(f"'{text4}'.isalpha() = {text4.isalpha()}")  # True

text5 = "hello123"
print(f"'{text5}'.isalpha() = {text5.isalpha()}")  # False

text6 = "Hello World"
print(f"'{text6}'.isalpha() = {text6.isalpha()}")  # False (has space)

text7 = ""
print(f"''.isalpha() = {text7.isalpha()}")  # False (empty)

# Practical example:
user_input = "username123"
if user_input.isalpha():
    print("Username contains only letters")
else:
    print("Username has numbers or special characters")
