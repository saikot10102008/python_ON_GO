# Encryption program that swaps characters using a shuffled lookup table.
import random
import string

# Build the full character set we want to support in the cipher.
characters = " " + string.punctuation + string.digits + string.ascii_letters
# Convert the string into a list so we can index into it character by character.
characters = list(characters)
# Create a second list that will become the shuffled mapping key.
key = characters.copy()

# Randomly rearrange the key so each character maps to a different one.
random.shuffle(key)

# Store the user's menu choice and start with an empty value.
choice = ""

# Keep showing the menu until the user chooses exit.
while choice.strip() != "3" and choice.strip().lower() != "exit":

    # Display the available actions.
    print("1. Encrypt \n2. Decrypt\n3. Exit")
    # Read the user's selection.
    choice = input("Your Choice: ")

    # Encrypt when the user selects option 1 or types the word encrypt.
    if (choice == "1" or choice.strip().lower() == "encrypt"):
        # Read the text that needs to be encrypted.
        plain_text = input("Plain text: ")
        # Start with an empty encrypted result.
        cipher_text = ""

        # Replace every character with its shuffled counterpart.
        for x in plain_text:
            # Find the current character's position in the original list.
            index = characters.index(x)
            # Append the matching character from the shuffled key.
            cipher_text += key[index]
        
        # Show the final encrypted text.
        print(f"Cipher Text: [{cipher_text}]")

    # Decrypt when the user selects option 2 or types the word decrypt.
    elif(choice == "2" or choice.strip().lower() == "decrypt"):
        # Start with an empty decrypted result.
        plain_text = ""
        # Read the text that needs to be decrypted.
        cipher_text = input("Plain text: ")

        # Reverse the mapping by looking up each cipher character in the key.
        for x in cipher_text:
            # Find the current character's position in the shuffled key.
            index = key.index(x)
            # Append the original character from the base character list.
            plain_text += characters[index]
        
        # Show the final decrypted text.
        print(f"Plain Text: [{plain_text}]")

    # Handle anything that is not the exit command and is not a valid menu option.
    elif choice.strip() != "3" and choice.strip().lower() != "exit":
        
        print("Error! Try again")
        