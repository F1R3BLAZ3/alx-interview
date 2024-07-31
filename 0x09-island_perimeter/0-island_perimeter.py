#!/usr/bin/python3
"""
This module contains a function to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island in the given grid.

    Args:
        grid (list of list of int): The grid representing the island and water. 
                                    0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the four adjacent cells
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1  # Check above
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1  # Check below
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1  # Check left
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1  # Check right
    return perimeter
