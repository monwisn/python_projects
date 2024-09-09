import secrets
import random
import string


class Password:
    # As always the initializer returns None
    def __init__(self, length: int = 12, use_uppercase: bool = True, use_special_chars: bool =True) -> None:
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_special_chars = use_special_chars

        # Get characters form string module
        self.base_characters: str = string.ascii_lowercase + string.digits

        # Check whether the user wants uppercase symbols or uppercase characters and symbols included in their password.
        if self.use_uppercase:
            self.base_characters += string.ascii_uppercase
        if self.use_special_chars:
            self.base_characters += string.punctuation

    # Initialize the password as an empty list
    def generate(self) -> str:
        password: list[str] = []

        for i in range(self.length):
            # We use the secrets module and the choice method which will pick a random element from any iterable.
            password.append(secrets.choice(self.base_characters))

        return ''.join(password)  # that will convert our list to a string


def main():
    password: Password = Password(length=12)
    print(password.generate())

    password2: Password = Password(length=16, use_uppercase=False)
    print(f' Only lowercase: {password2.generate()}, {password2.length} chars')

    password3: Password = Password(length=10, use_special_chars=False)
    print(f' With no special characters: {password3.generate()}, {password3.length} chars')

    for i in range(5):
        generated: str = password.generate()
        print(f'{generated}: {len(generated)} (chars)')


if __name__ == '__main__':
    main()
