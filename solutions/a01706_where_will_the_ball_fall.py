"""
Problem:
    1706. Where Will the Ball Fall
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/where-will-the-ball-fall
Tags:
    Array, Dynamic Programming, Depth-First Search, Matrix, Simulation
Date:
    2022-08-24T17:48:07.442750+08:00
"""
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        for start_index in range(len(grid[0])):
            start = start_index
            for row in grid:
                if 0 <= start + row[start] < len(row):
                    if row[start] != row[start + row[start]]:
                        start = -1
                        break
                else:
                    start = -1
                    break
                start += row[start]
            ans.append(start)
        return ans


tests = [
    (
        ([[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]],
         ),
        [1, -1, -1, -1, -1],
    ),
    (
        ([[-1]],
         ),
        [-1],
    ),
    (
        ([[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]],
         ),
        [0, 1, 2, 3, 4, -1],
    ),
]
