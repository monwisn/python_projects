
# Create the translation table that covers the entire alphabet and the numbers, each letter and number is mapped
# to these characters.
morse_code_dict: dict[str, str] = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----', ' ': '/'
}

# Reverse dictionary for decoding Morse code back to text
reverse_morse_code_dict: dict[str, str] = {value: key for key, value in morse_code_dict.items()}


def convert_to_morse(text: str) -> str:
    # We're using a comprehension that taking one char at a time out of our text and inserting it into the get method,
    # if it doesn't find that character, it's going to return an empty string.
    return ' '.join(morse_code_dict.get(char.upper(), '') for char in text)


# Function to decode Morse code back to regular text
def convert_from_morse(morse_code: str) -> str:
    return ''.join(reverse_morse_code_dict.get(word, '') for word in morse_code.split(' '))


def main():
    user_input: str = input('Enter a text to convert to Morse code: ')
    output: str = convert_to_morse(user_input)

    # print(f'Morse code: {convert_to_morse(user_input)}')
    print(f'Morse code: {output}')

    print(f'From morse code to text: {convert_from_morse(output).lower()}')


if __name__ == '__main__':
    main()
