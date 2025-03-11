import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)

        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints
        if all(
                constraint <= len(re.findall(pattern, password))
                for constraint, pattern in constraints
        ):
            break

    return password


def password_generation_menu():
    generated_password_counter = 0
    number_of_generated_passwords = int(input('How many passwords would you like generated?: '))
    length_of_password = int(input('Input length of password: '))
    number_of_numbers = int(input('Input number of numbers in password: '))
    number_of_special_chars = int(input('Input number of Special Characters in password: '))
    number_of_uppercase = int(input('Input number of UPPERCASE characters in password: '))
    number_of_lowercase = int(input('Input number of lowercase characters in password: '))

    while generated_password_counter < number_of_generated_passwords:
        new_password = generate_password(
            length_of_password, number_of_numbers, number_of_special_chars,number_of_uppercase, number_of_lowercase)
        print('Generated password:', new_password)
        generated_password_counter += 1


password_generation_menu()