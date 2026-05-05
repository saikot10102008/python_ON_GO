# What is a Library?
# A library is a collection of pre-written code that you can reuse in your program.
# Instead of writing everything from scratch, libraries provide ready-made functions
# and tools that save time and effort.

# Example: the `random` library has a function `randint()` that generates
# random numbers without you having to write the logic yourself.

import random

# Using the library's function:
secret = random.randint(1, 10)
tries = 0


while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret:
        print("You got it right!")
        tries+=1
        break
    else:
        print(f"Wrong!")
        tries+=1
    
    if (guess > secret):
        print("Go a little lower")
    else:
        print("Go a little higher")


print(f"It took you {tries} tries")