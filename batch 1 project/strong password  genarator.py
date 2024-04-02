import random
import string

def generate_password(length=12):
    # Define the character sets
    numbers = string.digits
    upper_case_letters = string.ascii_uppercase
    lower_case_letters = string.ascii_lowercase
    symbols = '!@#$%^&*()-_=+[]{}|;:,.<>?'

    # Combine all character sets
    all_chars = numbers + upper_case_letters + lower_case_letters + symbols

    # Ensure each character set is represented at least once
    password = random.choice(numbers)
    password += random.choice(upper_case_letters)
    password += random.choice(lower_case_letters)
    password += random.choice(symbols)

    # Generate the remaining characters randomly
    for _ in range(length - 4):
        password += random.choice(all_chars)


    # Shuffle the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

# Example usage:
length = int(input("Enter the length of the password: "))
password = generate_password(length)
print("Generated Password:", password)
