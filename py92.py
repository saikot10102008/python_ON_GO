# if __name__ == "__main__" in Python - Explained Simply & Thoroughly
# This is a very important and common pattern in Python scripts.

# --------------------
# WHAT DOES IT MEAN?
# --------------------
# When Python runs a file, it automatically sets a special variable called __name__
# - If you RUN the file directly (python script.py), then __name__ becomes "__main__"
# - If you IMPORT the file from another script, then __name__ becomes the module's name (e.g. "my_module")

# This allows a single file to work both as:
#   1. A standalone program (when run directly)
#   2. A reusable module (when imported by other files)

print("This line always runs, no matter what.")

# --------------------
# THE BASIC STRUCTURE
# --------------------

def favorite_food(food):
    """A simple function that can be reused"""
    print(f"Your favorite food is {food}!")


def main():
    """This function contains the code that should run only when the script is executed directly"""
    print("=== Starting the main program ===")
    favorite_food("pizza")
    favorite_food("sushi")
    print("Program finished successfully!")


# The magic line:
if __name__ == "__main__":
    main()          # Call the main function only when running this file directly

# --------------------
# WHY IS THIS USEFUL?
# --------------------

# 1. Prevents code from running when the file is imported
# 2. Makes your code more organized and professional
# 3. Allows the same file to be both a library and a runnable script
# 4. Improves readability - you can clearly see what the "entry point" is

# --------------------
# WITHOUT if __name__ == "__main__" (Bad Practice)
# --------------------

# If you just put code at the bottom without protection:

print("This would run even if someone imports this file!")

favorite_food("ice cream")   # This would also run on import - not good!

# --------------------
# FULL EXAMPLE WITH MULTIPLE FUNCTIONS
# --------------------

def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


def main():
    """Main entry point of the program"""
    print("Welcome to the Calculator Program!")
    
    result1 = add_numbers(5, 7)
    print(f"5 + 7 = {result1}")
    
    result2 = multiply_numbers(6, 8)
    print(f"6 * 8 = {result2}")
    
    print("Thank you for using the calculator!")


# Only run main() when this file is executed directly
if __name__ == "__main__":
    main()

# --------------------
# HOW IT WORKS WHEN IMPORTED
# --------------------

# Suppose another file (e.g. another_script.py) does this:
# import this_file_name
#
# Then:
# - The functions (favorite_food, add_numbers, etc.) become available
# - But the code inside if __name__ == "__main__": does NOT run
# - This keeps your module clean

# --------------------
# BEST PRACTICES
# --------------------
# - Always put your main logic inside a main() function
# - Use if __name__ == "__main__": to call main()
# - This pattern is used in almost all professional Python code
# - It helps avoid accidental execution of code when importing
# - Makes testing and reusing code much easier

# --------------------
# COMMON QUESTIONS
# --------------------
# Q: Can I put code directly under the if statement instead of calling main()?
# A: Yes, but using a main() function is cleaner and more organized.

# Q: What is __name__?
# A: A built-in variable that Python sets automatically.

# Q: What happens if I forget this line?
# A: Your code may run unwanted parts when imported by other files.

# Summary:
# - if __name__ == "__main__": protects the main code
# - Allows file to be both executable script AND importable module
# - Highly recommended for all Python scripts
# - One of the first "Pythonic" patterns beginners should learn