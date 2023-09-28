#!/usr/bin/python3
"""
Returns integers that represent Paschal's triangle.
"""


def pascal_triangle(n):
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        angle = []
        for j in range(i + 1):
            if j == 0 or j == i:
                angle.append(1)
            elif i > 0 and j > 0:
                angle.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(angle)
    return triangle