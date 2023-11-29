#!/usr/bin/python3
"""returns the perimeter of the island described in grid
"""
def island_perimeter(grid):
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:  # Land celfl
                perimeter += 4  # Assume all sides are part of the perimeter

                # Check adjacent cells and subtract if they are also land cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract two sides for adjacent land cell to the north
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract two sides for adjacent land cell to the west

    return perimeter
