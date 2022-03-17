import random
from string import digits, punctuation, ascii_lowercase, ascii_uppercase

all_combinations_from_digits_letters_symbols = digits + punctuation + ascii_uppercase + ascii_lowercase

password_length = input("Enter the password length: ")

password = ''.join(random.sample(all_combinations_from_digits_letters_symbols, password_length))

print(f"This is your password: {password}")
