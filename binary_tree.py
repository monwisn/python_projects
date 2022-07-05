# Creating binary tree from given list

from binarytree import build

# List of nodes

# nodes = [1, 3, 2, 8, 1, 1, 1, 4, 3, 3, 5, 5, 8, 3, 5, 5, 3, 3, 2, 2, 3]
nodes = [9, 2, 7, 2, 9, 9, 1, 2, 6, 6, 8, 8, 6]

# Building the binary tree

binary_tree = build(nodes)
print('Binary tree from list :\n', binary_tree)

# Getting list of nodes from binarytree

print('\nList from binary tree :', binary_tree.values)

# Python program for recursive implementation of max sum problem in a triangle

N = 4


#  Function for finding maximum sum

def max_path_sum(tri, x, y, row, col):
    if y == col:
        return 0

    if x == row - 1:
        return tri[x][y]

    return tri[x][y] + max(max_path_sum(tri, x + 1, y, row, col),
                           max_path_sum(tri, x + 1, y + 1, row, col))


# Driver program to test above functions
tri = [[4], [4, 7], [5, 8, 8], [9, 2, 7, 7], [4, 7, 4, 8, 2], [9, 5, 6, 9, 9, 9], [6, 9, 5, 3, 2, 1, 3],
       [8, 8, 1, 8, 2, 3, 6, 4], [1, 6, 5, 4, 7, 9, 8, 8, 9], [9, 3, 6, 8, 2, 5, 1, 4, 1, 2],
       [2, 3, 5, 3, 2, 9, 9, 4, 7, 7, 5], [7, 7, 2, 7, 3, 1, 5, 5, 8, 6, 5, 3], [3, 6, 9, 3, 1, 8, 7, 2, 7, 6, 9, 2, 5],
       [8, 3, 9, 9, 6, 7, 4, 6, 1, 2, 5, 1, 5, 9], [4, 8, 5, 7, 8, 5, 1, 7, 1, 6, 3, 4, 5, 6, 8]]

print(max_path_sum(tri, 0, 0, 15, 15))
