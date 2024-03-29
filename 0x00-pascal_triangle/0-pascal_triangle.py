#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(n):
    """
    Returns a list of lists.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        List[List[int]]:
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
        row.append(1)
        triangle.append(row)

    return triangle
