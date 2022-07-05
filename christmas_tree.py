def draw_christmas_tree():
    for row in range(1, 10):
        print(" " * (10 - row) + "*" * (row * 2 - 1))


draw_christmas_tree()
