# ========================================================
# range() FUNCTION + FOR LOOPS + STRING ITERATION + continue, break, and else in for loops
# ========================================================

print("=== PYTHON: range() + FOR LOOPS + STRING ITERATION + continue/break/else ===")
print("All concepts explained with examples from the video style\n")

# ========================================================
# 1. THE range() FUNCTION - FULL EXPLANATION
# ========================================================
# range() is a built-in function that generates a sequence of numbers.
# It is IMMUTABLE and MEMORY-EFFICIENT (does NOT create a list in memory).
# Syntax:
#   range(stop)              → 0 to stop-1
#   range(start, stop)       → start to stop-1
#   range(start, stop, step) → start to stop-1, increment by step
#
# Key points from the video:
# - stop value is EXCLUSIVE (never included)
# - step can be positive or negative
# - Very commonly used with for loops
# - range() returns a range object, not a list (use list() to see all values)

print("1. range() FUNCTION EXAMPLES:")
print("range(5)          →", list(range(5)))           # [0, 1, 2, 3, 4]
print("range(2, 8)       →", list(range(2, 8)))        # [2, 3, 4, 5, 6, 7]
print("range(1, 10, 2)   →", list(range(1, 10, 2)))    # [1, 3, 5, 7, 9]
print("range(10, 0, -2)  →", list(range(10, 0, -2)))   # [10, 8, 6, 4, 2]
print("range(0)          →", list(range(0)))           # [] (empty)
print("-" * 50)

# ========================================================
# 2. THE for LOOP - BASIC SYNTAX
# ========================================================
# for variable in iterable:
#     # code to run for each item
#
# iterable = anything you can loop over (list, tuple, string, range, etc.)
# The loop variable takes each value one by one.

print("2. BASIC for LOOP EXAMPLES:")
for i in range(5):
    print("  Count:", i)

print("\nFor loop with list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("  I like", fruit)
print("-" * 50)

# ========================================================
# 3. ITERATING OVER A STRING - TWO WAYS
# ========================================================
# Way 1: Using index + range(len(string))   ← Most common in video
# Way 2: Directly iterating over the string ← Cleaner and Pythonic

name = "Python"

print("3. ITERATING OVER STRING - METHOD 1 (using index):")
for i in range(len(name)):
    print(f"  Index {i} → character '{name[i]}'")

print("\n3. ITERATING OVER STRING - METHOD 2 (directly):")
for char in name:
    print(f"  Character: '{char}'")
print("-" * 50)

# ========================================================
# 4. continue, break, and else in for loops
# ========================================================
# continue → skips the rest of the current iteration and goes to the next
# break    → completely exits the loop
# else     → runs ONLY if the loop finished normally (NO break was hit)
#           This is a Python-specific feature!

print("4. continue, break, and else DEMO")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\nExample A: Using 'continue' (skip even numbers)")
for num in numbers:
    if num % 2 == 0:
        continue          # skip this iteration
    print("  Odd number found:", num)

print("\nExample B: Using 'break' (stop at first number > 6)")
for num in numbers:
    if num > 6:
        break             # exit loop immediately
    print("  Number:", num)
else:
    print("  'else' block: This would run only if no break happened")

print("\nExample C: Using 'else' with for loop (no break)")
for num in range(5):
    print("  Processing", num)
else:
    print("  'else' block executed because loop completed normally (no break)")

print("\nExample D: 'else' does NOT run if break occurred")
for num in range(10):
    if num == 3:
        print("  Breaking at", num)
        break
else:
    print("  This else will NOT run because break was used")
print("-" * 50)

# ========================================================
# 5. REAL-WORLD COMBINED EXAMPLE
# ========================================================
print("5. COMBINED PRACTICAL EXAMPLE")
text = "Hello Python World!"

print("Iterating string with index + continue + break + else:")
for i in range(len(text)):
    if text[i] == " ":          # skip spaces
        continue
    if text[i] == "P":          # stop when we hit capital P
        print("  Found 'P' at index", i, "→ breaking")
        break
    print(f"  Index {i}: {text[i]}")
else:
    print("  Loop finished without hitting 'P'")

print("\n✅ End of range() + for loop + string iteration + control statements notes")