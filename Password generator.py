# Password generation and hashing utility.
# Provides functions to generate complex passwords, hash them securely,
# and verify passwords against their hashes.

import random
import string
import hashlib
import os

def generate_complex_password(length=16):
    """
    Generates a complex password with a specified length.

    The password will contain at least one lowercase letter, one uppercase letter,
    one digit, and one punctuation symbol.

    Args:
        length (int): The desired length of the password. Must be at least 4.
                      Defaults to 16.

    Returns:
        str: The generated complex password.

    Raises:
        ValueError: If length is less than 4.
    """
    if length < 4:
        raise ValueError("Password length should be at least 4 to include all character types.")

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation # Using string.punctuation for a standard set

    # Ensure at least one character from each set
    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with a random combination of all character sets
    all_chars = lower + upper + digits + symbols
    remaining_length = length - len(password_chars) # Corrected remaining length calculation
    for _ in range(remaining_length):
        password_chars.append(random.choice(all_chars))

    # Shuffle the resulting list to ensure randomness
    random.shuffle(password_chars)

    return "".join(password_chars)

def hash_password(password):
    """
    Hashes a password using PBKDF2-HMAC-SHA256 with a random salt.

    Args:
        password (str): The plain-text password to hash.

    Returns:
        str: A string containing the salt and the derived key (hash),
             both hex-encoded and separated by a colon (salt:hash).
    """
    salt = os.urandom(16)  # Generate a 16-byte salt
    # Use PBKDF2 for key derivation. 100,000 iterations is a common recommendation.
    derived_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    # Return salt and derived key, hex-encoded and separated by a colon
    return salt.hex() + ':' + derived_key.hex()

def verify_password(plain_password, stored_password_hash):
    """
    Verifies a plain-text password against a stored salt and hash.

    Args:
        plain_password (str): The plain-text password to verify.
        stored_password_hash (str): The stored string containing the salt and hash
                                    (expected format: salt_hex:hash_hex).

    Returns:
        bool: True if the password matches the hash, False otherwise.
    """
    try:
        salt_hex, original_derived_key_hex = stored_password_hash.split(':')
        salt = bytes.fromhex(salt_hex)
        original_derived_key = bytes.fromhex(original_derived_key_hex) # Not strictly needed for compare_digest
    except ValueError:
        # Handle cases where the stored_password_hash is not in the expected format
        # or hex decoding fails.
        return False

    # Re-compute the derived key using the stored salt and the provided password
    new_derived_key = hashlib.pbkdf2_hmac('sha256', plain_password.encode('utf-8'), salt, 100000)

    # Compare the derived keys using a timing attack resistant comparison
    return hashlib.compare_digest(new_derived_key, bytes.fromhex(original_derived_key_hex))


if __name__ == "__main__":
    print("--- Password Utility ---")
    choice = input("Generate a new complex password? (y/n): ").lower()

    if choice == 'y':
        # Using default length for simplicity as per instructions
        new_password = generate_complex_password()
        print(f"\nGenerated Password: {new_password}")

        hashed_new_password = hash_password(new_password)
        print(f"Stored Hashed Password (salt:hash): {hashed_new_password}")

        # Demonstrate verification
        print("\n--- Attempting to verify the generated password ---")
        is_verified = verify_password(new_password, hashed_new_password)
        print(f"Verification successful: {is_verified}")

        # Demonstrate verification with a wrong password
        print("\n--- Attempting to verify with a wrong password ---")
        wrong_password_example = "wrongpassword123"
        is_verified_wrong = verify_password(wrong_password_example, hashed_new_password)
        print(f"Verification of '{wrong_password_example}' successful: {is_verified_wrong}")

    else:
        print("Exiting password utility.")

    print("\nThis Tool Create By - DJSAVI ")
