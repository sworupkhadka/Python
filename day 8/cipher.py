# List of all lowercase alphabets
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]
# Ask the user whether they want to encode or decode a message
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# Ask the user to enter the message text
text = input("Type your message:\n").lower()  # convert to lowercase
# Ask how many positions each letter should be shifted
shift = int(input("Type the shift number:\n"))


#ENCRYPTION

def encrypt(original_text, shift_amount):
    """Encrypts a message by shifting each letter forward by shift_amount."""
    cipher_text = ""

    for letter in original_text:
        if letter in alphabet:
            # Find letter index and shift forward
            shifted_position = (alphabet.index(letter) + shift_amount) 
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            # Keep spaces and punctuation unchanged
            cipher_text += letter

    print(f"Encoded result: {cipher_text}")


#DECRYPTION

def decrypt(cipher_text, shift_amount):
#Decrypts a message by shifting each letter backward by shift_amount.
    decrypted_text = ""

    for letter in cipher_text:
        if letter in alphabet:
            # Find letter index and shift backward
            shifted_position = (alphabet.index(letter) - shift_amount) 
            shifted_position %= len(alphabet)
            decrypted_text += alphabet[shifted_position]
        else:
            # Keep spaces and punctuation unchanged
            decrypted_text += letter

    print(f"Decoded result: {decrypted_text}")

# -----------------------------
#        EXECUTE CIPHER
# -----------------------------
if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("Invalid input. Please type 'encode' or 'decode'.")




#shifted_position %= len(alphabet)
# is Python shorthand for:
# shifted_position = shifted_position % len(alphabet)

# 🔹 What it does
# len(alphabet) → gives the total number of letters in the alphabet, which is 26.
# % is the modulo operator, which gives the remainder after division.
# So this line wraps the position around if it goes past the end of the alphabet.

# 🔹 Example in context
# Say we have 'z' (last letter, index 25) and shift it by 5:
# shifted_position = 25 + 5  # 30
# shifted_position %= 26      # 30 % 26 = 4
# Index 30 doesn’t exist in the alphabet (0–25).
# Using % 26 wraps it around to 4, which is 'e'.
# This is how Caesar cipher “rotates” through the alphabet without errors.

# 🔹 Summary
# % len(alphabet) ensures the letter index always stays within 0–25.

# It allows shifts beyond 'z' to wrap around to the beginning.