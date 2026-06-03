# =====================================================
# EMAIL SLICER PROGRAM
# Takes an email address and splits it into username and domain
# =====================================================

print("=== Email Slicer Program ===\n")

# Get email from user
email = input("Enter your email address: ").strip()

# Find the position of the @ symbol
at_index = email.find("@")

if at_index != -1:
    # Slice the username (everything before @)
    username = email[:at_index]
    
    # Slice the domain (everything after @)
    domain = email[at_index + 1:]
    
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Invalid email address! No '@' symbol found.")


print("\n=== Alternative using split() method ===\n")

# Alternative cleaner way using split()
email2 = input("Enter another email address: ").strip()

if "@" in email2:
    username2, domain2 = email2.split("@")
    print(f"Username: {username2}")
    print(f"Domain: {domain2}")
else:
    print("Invalid email address!")


print("\n=== Key Concepts Used ===\n")
print("• input()          : Get user input")
print("• .strip()         : Remove extra whitespace")
print("• .find('@')       : Find position of @ symbol")
print("• String slicing   : email[:index] and email[index+1:]")
print("• .split('@')      : Split string into list at @")
print("• if condition     : Check if @ exists")


print("\n=== All done! Email slicing complete! ===")