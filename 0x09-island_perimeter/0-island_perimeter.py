#!/usr/bin/python3
""" 0x09. Island Perimeter """


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Parameters:
    grid (List[List[int]]): A 2D list representing a map,
    where 0 represents water and 1 represents land.

    Returns:
    int: The perimeter of the island.

    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
