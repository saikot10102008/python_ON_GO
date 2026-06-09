# =====================================================
# ENCRYPTION USING PYTHON
# Encryption turns plain text into unreadable text with a key.
# Decryption turns the encrypted text back into readable text.
# Important: hashing is not encryption.
# =====================================================

# This is a simple educational example.
# It shows the idea of encryption, but it is not secure for real-world use.

print("=== Encryption in Python ===\n")

# This example uses a Caesar cipher.
# Each letter is shifted by a fixed number of positions.
# Real encryption should use a strong library and proper key management.

def encrypt(text, shift):
	# Build the encrypted text one character at a time.
	result = ""
	for char in text:
		if char.isalpha():
			# Preserve upper and lower case letters.
			base = ord("A") if char.isupper() else ord("a")
			result += chr((ord(char) - base + shift) % 26 + base)
		else:
			# Keep spaces, punctuation, and numbers unchanged.
			result += char
	return result


def decrypt(text, shift):
	# Decryption just shifts letters back in the opposite direction.
	return encrypt(text, -shift)


# Step 1: choose a shift value as the key.
shift = 3

# Step 2: write the message you want to protect.
message = "Hello, Python encryption!"
print("Original message:", message)

# Step 3: encrypt the message.
encrypted_message = encrypt(message, shift)
print("Encrypted message:", encrypted_message)

# Step 4: decrypt the message back to the original text.
decrypted_message = decrypt(encrypted_message, shift)
print("Decrypted message:", decrypted_message)


print("\n=== Key Notes ===\n")

# 1. Encryption changes readable text into unreadable text.
# 2. Decryption uses the key to get the original text back.
# 3. The Caesar cipher is only for learning, not for real security.
# 4. Real encryption should use strong algorithms and secret keys.

print("• Encryption = protect data with a key")
print("• Decryption = recover the original data")
print("• Hashing = one-way process, not reversible")


print("\n=== All done! ===")
