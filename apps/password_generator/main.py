import random
from colorama import Fore, init
init()
def gen_password():
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    symbols= '!@#$%^&*()*+-'
    caps_letters = letters.upper()
    password = ''
    for i in range(0, 16):
        password += random.choice(letters)
        password += random.choice(symbols)
        password += random.choice(caps_letters)
    return password, print(f'Your password: {Fore.GREEN}{password}')