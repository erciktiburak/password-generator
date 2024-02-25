import random
import string

def generate_password(length=12):
    # Define the character sets to use in the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

# Generate a password with default length (12 characters)
password = generate_password()
print("Generated Password:", password)