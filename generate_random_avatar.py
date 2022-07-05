# HTTP-API (generate your avatar based on entered name/string)

import requests
import random

from pathlib import Path


# change sprites and seed example below:
# requests.get('https://avatars.dicebear.com/api/:sprites/:seed.svg')
response = requests.get('https://avatars.dicebear.com/api/female/cherry123.svg')

# random generated seed:
gender = input('Enter your avatar gender: ')
random_response = requests.get(f'https://avatars.dicebear.com/api/{gender}/{random.random()}.svg')

# dot means current directory
Path('./avatars').mkdir(exist_ok=True)

# save file with avatar
with open('./avatars/avatar.svg', 'wb') as f:
    f.write(response.content)

with open('./avatars/avatar_random.svg', 'wb') as file:
    file.write(random_response.content)

quit()
