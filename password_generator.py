#password generator
print("welcome to password generator!")

import random
import string

def generate_password():
    num_letters = int(input("How many letters do you want? "))
    num_digits = int(input("How many numbers do you want? "))
    num_symbols = int(input("How many symbols do you want? "))


    letters = string.ascii_letters  # both lowercase + uppercase
    digits = string.digits
    symbols = "!@#$%^&*"

    password_symbols = random.choices(symbols, k=num_symbols)
    password_letters = random.choices(letters, k=num_letters)
    password_digits = random.choices(digits, k=num_digits)

    password = "".join(password_symbols + password_letters + password_digits)
    return password


print("Generated Password:", generate_password())
