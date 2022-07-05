# Duplicate words task

# Write a program that accepts a sequence of words and returns
# a sorted list whereby all duplicate words have been removed.

# We can use: set(), .split(), sorted()


sequence_of_words = input('Enter your words: ')
words = set(sequence_of_words.split(' '))

print(sorted(list(words)))

# or

sequence = input()
words = sequence.split(" ")

print(sorted(list(set(words))))
