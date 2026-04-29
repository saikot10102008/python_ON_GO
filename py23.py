# ============================================
# FOR LOOPS AND WHILE LOOPS IN PYTHON
# ============================================

# FOR LOOP: Iterates over a sequence (list, string, range, etc.)
# Syntax: for variable in sequence:
#         - Repeats block of code for each item
#         - Best when you know how many times to loop

# Example 1: Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 2: Loop through range (0 to n-1)
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# Example 3: Loop through string
for char in "hello":
    print(char)

# Example 4: Loop with enumerate (index and value)
for index, fruit in enumerate(fruits):
    print(index, fruit)

# ============================================
# WHILE LOOP: Repeats as long as condition is TRUE
# Syntax: while condition:
#         - Checks condition before each iteration
#         - Best when iterations depend on changing condition
#         - RISK: Infinite loop if condition never becomes False

# Example 1: Count up
count = 0
while count < 5:
    print(count)
    count += 1  # Must update condition, or infinite loop!

# Example 2: Loop until user input
# user_input = ""
# while user_input != "quit":
#     user_input = input("Enter 'quit' to exit: ")

# Example 3: Dangerous - Infinite Loop (don't run!)
# while True:
#     print("This runs forever!")

# ============================================
# KEY DIFFERENCES
# ============================================
# FOR:   - Loop over known sequence
#        - Automatically stops at end
#        - Can use break/continue
#
# WHILE: - Loop while condition is true
#        - Need to manually control condition
#        - Risk of infinite loops
#        - Can use break/continue
