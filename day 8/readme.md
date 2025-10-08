# Python Functions and Caesar Cipher

This README demonstrates Python functions with single and multiple parameters, a life-in-weeks calculator, a love score calculator, and a Caesar cipher implementation with encryption and decryption.

---

## Table of Contents
1. [Basic Functions](#basic-functions)
2. [Functions with Parameters](#functions-with-parameters)
   - [Functions with Multiple Parameters](#functions-with-multiple-parameters)
3. [Life in Weeks Calculator](#life-in-weeks-calculator)
4. [Love Score Calculator](#love-score-calculator)
5. [Caesar Cipher](#caesar-cipher)
   - [Alphabet and User Input](#alphabet-and-user-input)
   - [Encryption](#encryption)
   - [Decryption](#decryption)
   - [Execute Cipher](#execute-cipher)
   - [Modulo Explanation](#modulo-explanation)

---

## Basic Functions

```python
def greet():                            # defining a function
    print("hello")
    print("how do u do")
    print("im fine")
    greet()                                # calling a function


Functions with Parameters

def greet_with_name(name):
    print(f"hello {name}")
    print(f"how do u do {name}")
    print("im fine")
greet_with_name("sk")


Functions with Multiple Parameters

def greet_with(name, location):
    print(f"hello {name}")
    print(f"how is it like in {location}")
greet_with(name="sk", location="pokhara")

# or positional arguments
greet_with("sk", "Pokhara")   
# Note: swapping order may cause errors


Life in Weeks Calculator

def life_in_weeks(age):
    years_left = 90 - age
    weeks_left = years_left * 52
    print(f"You have {weeks_left} weeks left.")

# Call your function with a hard-coded value
life_in_weeks(23)



Love Score Calculator

def calculate_love_score(name1, name2):
    # Combine both names into a single string and lowercase it
    combined_names = (name1 + name2).lower()

    # Count letters in "TRUE"
    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")
    true_score = t + r + u + e

    # Count letters in "LOVE"
    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    e = combined_names.count("e")
    love_score = l + o + v + e

    # Combine into two-digit score
    total_score = int(str(true_score) + str(love_score))

    # Display final love score
    print(total_score)

# Test function
calculate_love_score("Kanye West", "Kim Kardashian")



Caesar Cipher
Alphabet and User Input


alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
Encryption
python
Copy code
def encrypt(original_text, shift_amount):
    """Encrypts a message by shifting letters forward."""
    cipher_text = ""

    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount)
            shifted_position %= len(alphabet)  # wrap around
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter  # keep spaces/punctuation

    print(f"Encoded result: {cipher_text}")
Decryption
python
Copy code
def decrypt(cipher_text, shift_amount):
    """Decrypts a message by shifting letters backward."""
    decrypted_text = ""

    for letter in cipher_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) - shift_amount)
            shifted_position %= len(alphabet)
            decrypted_text += alphabet[shifted_position]
        else:
            decrypted_text += letter

    print(f"Decoded result: {decrypted_text}")
Execute Cipher
python
Copy code
if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("Invalid input. Please type 'encode' or 'decode'.")


---
Modulo Explanation
# shifted_position %= len(alphabet)
# This is shorthand for:
# shifted_position = shifted_position % len(alphabet)

# 🔹 Purpose
# Ensures letter index stays within 0-25 (a-z)
# Allows wrap-around if shift exceeds 'z'

# 🔹 Example
# 'z' (index 25) shifted by 5:
# 25 + 5 = 30 → 30 % 26 = 4 → 'e'
pgsql



