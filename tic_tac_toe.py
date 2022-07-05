import sys

game_state = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def draw_a_frame():
    print(''.ljust(1, ' '), ''.ljust(1, '{0}'.format(*game_state)), ''.ljust(1, ' '), ''.ljust(1, '|'),
          ''.ljust(1, ' '),
          ''.ljust(1, '{1}'.format(*game_state)), ''.ljust(1, ' '), ''.ljust(1, '|'), ''.ljust(1, ' '),
          ''.ljust(1, '{2}'.format(*game_state)), ''.ljust(1, ' '))
    print(''.ljust(21, '-'))
    print(''.ljust(1, ' '), ''.ljust(1, '{3}'.format(*game_state)), ''.ljust(1, ' '), ''.ljust(1, '|'),
          ''.ljust(1, ' '),
          ''.ljust(1, '{4}'.format(*game_state)), ''.ljust(1, ' '), ''.ljust(1, '|'), ''.ljust(1, ' '),
          ''.ljust(1, '{5}'.format(*game_state)), ''.ljust(1, ' '))
    print(''.ljust(21, '-'))
    print(''.ljust(1, ' '), ''.ljust(1, '{6}'.format(*game_state)), ''.ljust(1, ' '), ''.ljust(1, '|'),
          ''.ljust(1, ' '),
          ''.ljust(1, '{7}'.format(*game_state)), ''.ljust(1, ' '), ''.ljust(1, '|'), ''.ljust(1, ' '),
          ''.ljust(1, '{8}'.format(*game_state)), ''.ljust(1, ' '))


draw_a_frame()


def switch_player(iter):
    if iter % 2 == 0:
        player = ['X']
    else:
        player = ['O']

    return player


def get_data(player):
    while True:
        field_num = input(f"Player {player} select a field (1-9): ")

        if not field_num.isnumeric():
            print("Field value not allowed", file=sys.stderr)
            continue

        elif field_num not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            print("Field value not allowed", file=sys.stderr)
            continue

        else:
            break

    return field_num


def save_game():
    if player[0] == 'X':
        for i in playerX:
            if i in game_state:
                game_state[game_state.index(i)] = 'X'

    elif player[0] == 'O':
        for i in playerO:
            if i in game_state:
                game_state[game_state.index(i)] = 'O'

    else:
        print("Error")


def check_game_save(player):
    while True:
        x = get_data(player)

        if player[0] == 'X':
            if x in playerX or x in playerO:
                print('Field taken')
                continue
            else:
                playerX.append(x)
                save_game()
                return x

        elif player[0] == "O":
            if x in playerX or x in playerO:
                print('Field taken')
                continue
            else:
                playerO.append(x)
                save_game()
                return x


winning_sets1 = ['1', '2', '3']
winning_sets2 = ['4', '5', '6']
winning_sets3 = ['7', '8', '9']
winning_sets4 = ['1', '4', '7']
winning_sets5 = ['2', '5', '8']
winning_sets6 = ['3', '6', '9']
winning_sets7 = ['1', '5', '9']
winning_sets8 = ['3', '5', '7']

sets = [winning_sets1, winning_sets2, winning_sets3, winning_sets4, winning_sets5, winning_sets6, winning_sets7,
        winning_sets8]


def check_the_result():
    if player[0] == "X":
        player_list = playerX
    else:
        player_list = playerO

    for x in range(len(sets)):

        bingo = 0

        for _ in sets[x]:
            if _ in player_list:
                bingo += 1

        if bingo == 3:
            return player[0]
        else:
            continue


def return_winning_set():
    if player[0] == "X":
        player_list = playerX
    else:
        player_list = playerO

    for x in range(len(sets)):

        bingo = 0

        for _ in sets[x]:
            if _ in player_list:
                bingo += 1

        if bingo == 3:
            return sets[x]

        else:
            continue


def draw():
    if len(playerX) + len(playerO) == 9:
        return True
    else:
        return


playerX = []
playerO = []
iter = 1

while True:
    player = switch_player(iter)
    x = check_game_save(player)

    winner = check_the_result()
    winning_set = return_winning_set()

    print("\n")

    draw_a_frame()

    print("\n")

    if winner:
        print(f"Player {player} has won!!! Congrats!")
        break
    if draw():
        print("Draw! Try again.")
        break
    print("\n")

    iter += 1
