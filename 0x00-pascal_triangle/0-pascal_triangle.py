"""
Module for generating Pascal's Triangle.

This module provides a function to generate Pascal's Triangle up to a specified
number of rows.

Functions:
- pascal_triangle(n): Generate Pascal's Triangle up to the given number of rows.

Usage:
>>> pascal_triangle(5)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the given number of rows.

    Parameters:
    - n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
    - List of Lists: A 2D list representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        # Initialize each row with 1s
        row = [1] * (i + 1)

        # Calculate the values inside the row (excluding the first and last element)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Append the current row to the triangle
        triangle.append(row)

    return triangle
