import string
import random
LETTERS = string.ascii_letters
NUMBERS = string.digits

def password_generate(length=64):
    chars = f'{LETTERS}{NUMBERS}'
    chars = list(chars)
    random.shuffle(chars)
    password = random.choices(chars, k=length)
    password = ''.join(password)
    return password

print(password_generate())
