# Message encryption/decryption

import string
import codecs


def translate_rot13() -> dict:
    lowercase: str = string.ascii_lowercase
    uppercase: str = string.ascii_uppercase

    shift: int = 13

    shift_lowercase: str = lowercase[shift:] + lowercase[:shift]
    shift_uppercase: str = uppercase[shift:] + uppercase[:shift]

    translator: dict = str.maketrans(lowercase + uppercase, shift_lowercase + shift_uppercase)

    return translator


print(translate_rot13())


def rot13(message: str) -> str:
    table: dict = translate_rot13()

    return message.translate(table)


encrypted: str = rot13('encrypted message')
print(encrypted)

decrypted: str = rot13(encrypted)
print(decrypted)


# We can also use module 'codecs'.
user_input: str = input('Your message: ')
encoded: str = codecs.encode(obj=user_input, encoding='rot13')
print(encoded)

decoded: str = codecs.decode(obj=encoded, encoding='rot13')
print(decoded)
