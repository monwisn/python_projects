"""Ticket Lottery
check in which time round you could win the lottery."""
import random

COST_OF_SINGLE_DRAW = 3
numbers = {16, 2, 26, 5, 37, 41}  # It's a set, numbers cannot be repeated
all_numbers = range(1, 50)


def draw_numbers():
    """Draw 6 lotto numbers

    Returns:
        set: collection with 6 different lottery numbers from range 1 to 49
    """
    return set(random.sample(all_numbers, k=6))


if __name__ == '__main__':
    random_numbers = {}  # change from list to set because the comparison must be on the same types
    COUNTER = 0

    while numbers != random_numbers:
        random_numbers = draw_numbers()
        COUNTER += 1  # at which time / loop rotation we hit the equality

    TOTAL_COST = COST_OF_SINGLE_DRAW * COUNTER

    print(f'The cost of investing in bets, at the amount of 3 PLN for one coupon, is: {TOTAL_COST:,} PLN.')
    print(f'Number of drawing attempts to win: {COUNTER:,}.')


def test_draw_numbers():
    """Test for file

    Returns:
        bool: returns True/False values
    """

    # given
    # when
    for _ in range(501):
        drawn_numbers = sorted(list(draw_numbers()))
        # then
        assert len(drawn_numbers) == 6
        assert drawn_numbers[0] >= 1
        assert drawn_numbers[-1] <= 49
