from collections import Counter

# Function that opens the text file
def open_file(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            text: str = file.read()
            return text

    except FileNotFoundError:
        return "File not found"

    except Exception as e:
        return f"An error occurred: {e}"


# Test the function with a valid file path
print(open_file('python mini projects/note.txt'))

# Test the function with an invalid file path
print(open_file('non_existent_file.txt'))

print()


# Function that analyzes the text file
def analyse(text: str) -> dict[str, int]:
    print(f'Text: {text}', end='\n\n')
    print("--- Analysis ---", end='\n\n')

    result: dict[str, int] = {
        'total_chars_incl_spaces': len(text),
        'total_chars_excl_spaces': len(text.replace(' ', '')),
        'total_spaces': text.count(' '),
        'total_words': len(text.split()),  # split converts a string into different parts
        'total_unique_words': len(set(text.split())),
        'most_common_words': Counter(text.split()).most_common(4)
    }

    return result


def main():
    text: str = open_file('python mini projects/note.txt')
    analysis: dict[str, int] = analyse(text)

    for key, value in analysis.items():
        print(f"{key}: {value}")


if __name__ == '__main__':
    main()
