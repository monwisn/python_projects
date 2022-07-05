# The simple quiz with questions in a json file

import json

points = 0


def show_questions(quest):
    global points
    print()
    print(quest['question'])
    print('a', quest['a'])
    print('b', quest['b'])
    print('c', quest['c'])
    print('d', quest['d'])
    print()

    answer = input('Which answer do you choose: ')

    if answer == quest['correct_answer']:
        points += 1
        print(f"That's the correct, you already have {points} points, bravo!")

    else:
        print("Unfortunately, that's the wrong answer, the correct answer is:", quest['correct_answer'])


with open('quiz_questions.json') as json_file:
    questions = json.load(json_file)

    for i in range(0, len(questions)):
        show_questions(questions[i])

print()
print(f"Game over! You scored {points} points.")
