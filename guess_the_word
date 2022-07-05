# Simple guess the word game:

import random

words_to_guess = ["pineapple", "pear", "banana", "grape", "kiwi", "lemon", "orange", "apple", 'grapefruit', 'raspberry',
                  'peach', 'melon', 'strawberry', 'watermelon', 'blueberry', 'cherry', 'blackberry', 'coconut', 'plum']


def start_game():
    start = input("If you would like to start game press 'y' or quit then press 'q': ").lower()
    if start == 'y':
        tries = 10
        player_name = input('Enter your name: ')
        random_word = list(random.choice(words_to_guess))
        display_word = ['_ '] * len(random_word)

        print('\nYou have 12 tries to guess the word. Each incorrect letter entered means one less try.')
        print(f'Good luck {player_name}!')
        print(f'Your word to guess has {len(random_word)} letters (category: fruits).\n')
        print('_ ' * len(random_word))

        while tries > 0 and random_word != display_word:
            guess_letter = input("\nEnter letter to guess the word: ")

            if guess_letter in random_word:

                for index, letter in enumerate(random_word):
                    if letter == guess_letter:
                        display_word[index] = letter
            else:
                tries -= 1

            print(' '.join(display_word))

            print(f'\nThe remaining tries: {tries}')

            if random_word == display_word:
                print(f'Congrats {player_name}! You won. Your guessed word is: {"".join(display_word)}.')

            if tries == 0:
                print("You've lost!")
        quit()

    elif start == 'q':
        print('Bye bye then!')
        quit()

    else:
        print('Unknown command, please try again: ')
        start_game()


if __name__ == '__main__':
    start_game()
