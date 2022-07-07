# Program to encrypt passwords, words, with an offset

key_letter = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(letter, shift):
    new_index = key_letter.index(letter) + shift
    return key_letter[new_index]


print(encrypt("b", 3))  # result is e, shift by 3


def encrypt_word(word, shift):
    encrypted_word = ''
    for letter in word:
        new_index = key_letter.index(letter) + shift
        encrypted_word += key_letter[new_index]
    return encrypted_word


print(encrypt_word('mon', 4))


# Using alphabet import and protection against moving beyond the range of the alphabet i.e. return to start a, b, c ..
import string

key_lett = string.ascii_letters  # or lowercase


def encrypt(word, shift):
    encrypted_word = ''
    for letter in word:
        new_index = key_lett.index(letter) + shift
        encrypted_word += key_lett[new_index]
    return encrypted_word


word = input("Enter word to encrypt: ")
shift = int(input("Enter what the offset should be: "))

print(encrypt(word, shift))


# With dictionary use
import string

alphabet = string.ascii_letters


def encrypt(word, shift):
    key_val = {}
    for letter in word:
        new_index = (alphabet.index(letter) + shift) % len(alphabet)
        key_val[letter] = alphabet[new_index]
    return key_val


encrypted = encrypt('something', 3)
print(encrypted)


# encryption and decryption
import string


alphab = string.ascii_letters


def encrpytion(word, shift):
    key_v = {}
    for letter in word:
        new_index = (alphab.index(letter) + shift) % len(alphab)
        key_v[letter] = alphab[new_index]

    encrypted_word = ''
    for letter in word:
        encrypted_word += key_v[letter]

    return encrypted_word


def decryption(word, shift):
    key = {}
    for letter in alphab:
        new_index = (alphab.index(letter) + shift) % len(alphab)
        key[alphab[new_index]] = letter

    encrypted_word = ''
    for letter in word:
        encrypted_word += key[letter]

    return encrypted_word


before_encryption = input('Enter the word: ')
print(f'The word before encryption: {before_encryption}')

encrypted = encrpytion(before_encryption, 3)
print(f'After encryption: {encrypted}')
print(f'After decryption: {decryption(encrypted, 3)}')
