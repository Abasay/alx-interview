#!usr/bin/python
"""
Task 0X07 rotate the matrix
"""


def rotate_2d_matrix(matrix):
    """
    Function that rotates a matrix
    """
    index = 0

    resList = []
    for elem in range(0, len(matrix)):
        newList = []
        for row in matrix:
            newList.append(row[index])
        index += 1
        newList.reverse()
        resList.append(newList)
    return resList


print(rotate_2d_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

print(
    rotate_2d_matrix(
        [[1, 11, 13, 19], [41, 32, 6, 22], [55, 21, 41, 66], [77, 29, 78, 2]]
    )
)

print(
    rotate_2d_matrix(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
    )
)

print(
    rotate_2d_matrix(
        [
            [5, 8, 11, 14, 17, 20],
            [23, 26, 29, 32, 35, 38],
            [41, 44, 47, 50, 53, 56],
            [59, 62, 65, 68, 71, 74],
            [77, 80, 83, 86, 89, 92],
            [95, 98, 101, 104, 107, 110],
        ]
    )
)
