# Create a secure random password using Python

import random
from string import digits
from string import punctuation
from string import ascii_letters


password: str = ''
symbol = ascii_letters + digits + punctuation
secure_random = random.SystemRandom()

for _ in range(20):
    password += ''.join((secure_random.choice(symbol)))
print(password)
