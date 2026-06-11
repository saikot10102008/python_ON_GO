#  Encryption Program
import random
import string

characters = " " + string.punctuation + string.digits + string.ascii_letters
characters = list(characters)
key = characters.copy()

random.shuffle(key)

choice = ""

while choice.strip() != "3" and choice.strip().lower() != "exit":

    print("1. Encrypt \n2. Decrypt\n3. Exit")
    choice = input("Your Choice: ")

    if (choice == "1" or choice.strip().lower() == "encrypt"):
        # pass
        plain_text = input("Plain text: ")
        cipher_text = ""

        for x in plain_text:
            index = characters.index(x)
            cipher_text += key[index]
        
        print(f"Cipher Text: [{cipher_text}]")

    elif(choice == "2" or choice.strip().lower() == "decrypt"):
        # pass
        plain_text = ""
        cipher_text = input("Plain text: ")

        for x in cipher_text:
            index = key.index(x)
            plain_text += characters[index]
        
        print(f"Plain Text: [{plain_text}]")

    elif choice.strip() != "3" and choice.strip().lower() != "exit":
        
        print("Error! Try again")
        