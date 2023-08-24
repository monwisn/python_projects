# one line password generator
import random
import string

password = ''.join(random.choice(string.ascii_letters) for _ in range(10))
print(password)

# with special characters and numbers
password = ''.join(random.choice(string.ascii_letters + string.punctuation + string.digits) for _ in range(20))
print(password)

# generate password
import sys
import random
import string

password: list = []
characters_left: int = -1


def update_characters_left(number_of_characters):
    global characters_left
    if number_of_characters < 0 or number_of_characters > characters_left:
        print('Number of characters outside the range 0 :', characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print('Characters left:', characters_left)


password_length = int(input('How long the password should be: '))

if password_length < 7:
    print('The password should be at least 7 characters long (including at least 1 capital letter, 1 number and 1 special character')
    sys.exit(0)
else:
    characters_left = password_length

lowercase_letters = int(input('How many lowercase letters the password should have:'))
update_characters_left(lowercase_letters)

uppercase_letters = int(input('How many uppercase letters the password should have: '))
update_characters_left(uppercase_letters)

special_characters = int(input('How many special characters the password should have: '))
update_characters_left(special_characters)

digits = int(input('How many digits the password should have:  '))
update_characters_left(digits)

if characters_left > 0:
    print('Not all characters have been used. The password will be completed in lowercase.')
    lowercase_letters += characters_left

print()
print('Password length:', password_length)
print('Lowercase:', lowercase_letters)
print('Uppercase:', uppercase_letters)
print('Special characters:', special_characters)
print('Digits:', digits)

for _ in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

# The shuffle function will make all the characters mixed.
random.shuffle(password)

# The password will be displayed in the form of a list, to create a string from it, you need to use the .join function.
print('The generated password is:', ''.join(password))
