# Word Frequency Counter - If we were to insert a block of text, it's going to be able to extract the words
# and count how many occurrences of each word there is in that that text block.

import re
from collections import Counter


def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()

    # simple regex code to find all the words in the sentence which are alphanumeric and which contain underscores
    words: list[str] = re.findall(r'\b\w+\b', lowered_text)
    word_counts: Counter = Counter(words)

    return word_counts.most_common(n=5)  # n=5 - how many of the most common words you want to retrieve


def main():
    # depending on what the user enters we're going to want to strip the leading and trailing whitespaces
    # text: str = "Hello, world! This is a sample text for word frequency counting. Hello again!"
    text_input: str = input("Enter a text block: ").strip()
    word_frequencies: list[tuple[str, int]] = get_frequency(text_input)

    # print(f"Word Frequency: {word_frequencies}")
    for word, count in word_frequencies:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
