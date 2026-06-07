# =====================================================
# RANDOM NUMBERS IN PYTHON
# Using the random module for generating random values
# =====================================================

import random  # Import the random module

print("=== Random Numbers in Python ===\n")

# 1. random.random() - Returns a random float between 0.0 and 1.0 (not including 1.0)
print("Random float (0.0 to 1.0):", random.random())

# 2. random.randint(a, b) - Random integer between a and b (inclusive)
print("Random integer 1-10:", random.randint(1, 10))
print("Random integer 1-100:", random.randint(1, 100))

# 3. random.randrange(start, stop, step) - Random number from range
print("Random even number 2-20:", random.randrange(2, 21, 2))

# 4. random.choice(sequence) - Pick a random item from a list/tuple/string
options = ['Rock', 'Paper', 'Scissors']
print("Random choice from list:", random.choice(options))

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
print("Random playing card:", random.choice(cards))

# 5. random.shuffle(sequence) - Shuffles a list in place
deck = cards[:]  # Copy the list
random.shuffle(deck)
print("Shuffled deck:", deck)


print("\n=== Number Guessing Game ===\n")

# Simple number guessing game
import time  # Optional: for a small delay

low = 1
high = 20
number = random.randint(low, high)
guesses = 0
guess = 0

print(f"Guess the number between {low} and {high}!")

while True:
    guess = int(input("Enter your guess: "))
    guesses += 1
    
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You got it in {guesses} guesses!")
        break


print("\n=== More Random Examples ===\n")

# Random float between two values
print("Random float 5.0 to 10.0:", random.uniform(5.0, 10.0))

# Simulate rolling a die
def roll_dice():
    return random.randint(1, 6)

print("Dice roll:", roll_dice())
print("Dice roll:", roll_dice())


print("\n=== Key Functions from random module ===\n")
print("• random.random()     → float 0.0 <= x < 1.0")
print("• random.randint(a,b) → integer a to b inclusive")
print("• random.randrange()  → like range() but random")
print("• random.choice(seq)  → pick one item")
print("• random.shuffle(seq) → shuffle list in place")
print("• random.uniform(a,b) → float between a and b")


print("\n=== All done! Randomness in Python is easy and fun! ===")