# Simple Gallows Game

import random


gallows = ("""
  ____
  |   |
  |
  |
  |
  |
____________""", """
  ____
  |   |
  |   o
  |
  |
  |
____________
""", """
  ____
  |   |
  |   o
  |  /
  |
  |
_____________
""", """
  ____
  |   |
  |   o
  |  /|
  |
  |
_____________
""", """
  ____
  |   |
  |   o
  |  /|
  |
  |
_____________
""", """
  ____
  |   |
  |   o
  |  /|\\
  |  /
  |
_____________
""", """
  ____
  |   |
  |   o
  |  /|\\
  |  / \\
  |
____________
""")


words_list = ["pineapple", "pear", "banana", "grape", "kiwi", "lemon", "orange", "watermelon", 'lime']


# game

random_word = random.choice(words_list)
print(f'Your word to guess has: {len(random_word)} letters')
print()

for letter in random_word:
    print('_ ', end='')


print('')

word_to_guess = len(random_word) * '_'
guess = []

mistakes = 0

while True:
    if mistakes > 6:
        print("You lost!")
        break

    if set(guess) == set(random_word):
        print("You won!")
        break

    typed_letter = input("Enter the letter: ")

    if typed_letter.isdigit():
        print("You must enter the letter!")

    elif len(typed_letter) > 1:
        print("Error! Please enter one letter")

    else:
        if typed_letter in random_word:
            guess.append(typed_letter)

    if typed_letter in random_word:
        a = ''
        for i in range(len(random_word)):
            if typed_letter == random_word[i]:
                a += typed_letter
            else:
                a += word_to_guess[i]

        word_to_guess = a

        for i in range(len(word_to_guess)):
            print(word_to_guess[i], ' ', end='')
        print('')
    else:
        print(gallows[mistakes])
        mistakes += 1
