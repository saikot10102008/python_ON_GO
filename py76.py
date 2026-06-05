# =====================================================
# COUNTDOWN TIMER PROGRAM
# A digital countdown timer in HH:MM:SS format
# =====================================================

import time  # For the sleep function (pauses execution)

print("=== Countdown Timer ===\n")

# Get time from user in seconds
my_time = int(input("Enter the time in seconds: "))

print("\nCountdown starting...\n")

# Count down from my_time to 1
for x in range(my_time, 0, -1):
    # Calculate hours, minutes, seconds
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    
    # Display in HH:MM:SS format with zero padding
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    
    # Pause for 1 second
    time.sleep(1)

print("\nTIME'S UP! ⏰")


print("\n=== Alternative Version with Clear Screen (Advanced) ===\n")

# This version overwrites the previous line instead of printing new lines each second
import os

my_time = int(input("Enter another time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    
    # Clear the console (works on most systems)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("\nTIME'S UP! ⏰")


print("\n=== Key Concepts Used ===\n")
print("• import time          : Access time.sleep()")
print("• time.sleep(1)        : Pause program for 1 second")
print("• range(start, stop, step) : Count backwards with negative step")
print("• Modulo operator %    : Get remainder (seconds % 60)")
print("• Integer division     : Convert total seconds to minutes/hours")
print("• Format specifiers    : :02 for zero-padded 2 digits")
print("• f-strings            : Display formatted time")


print("\n=== All done! Great practice with loops and time! ===")