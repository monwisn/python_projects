from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Nothing in there'
    elif 'hello' in lowered:
        return f'Hello from the other side hihi!'
    elif 'hi' in lowered:
        return f'Hi there!'
    elif 'goodbye' in lowered or 'bye' in lowered:
        return f'See you!'
    elif 'how are you?' in lowered:
        return f'Good, thanks for asking!'
    elif 'roll dice' in lowered:
        return f'You rolled a {randint(1, 6)}'
    else:
        return choice(['I don\'t understand what you mean',
                       'What are you taking about?',
                       'Do you mind rephrasing that?',
                       'Could you please ask me again?',
                       'I\'m sorry, I didn\'t get that.',
                       ])  # choice pick a random one each time we run into this else block

    # raise NotImplementedError('Code not implemented')
