"""
Problem:
    54. Spiral Matrix
Difficulty:
    Medium
URL:
    https://leetcode.com/problems/spiral-matrix
Tags:
    Array, Matrix, Simulation
Date:
    2022-08-24T16:46:14.562345+08:00
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        new_matrix = []
        while matrix:
            if matrix:
                new_matrix += matrix.pop(0)
            for i, m in enumerate(matrix):
                if matrix[i]:
                    new_matrix.append(matrix[i].pop())
            if matrix:
                new_matrix += reversed(matrix.pop())
            for i in range(len(matrix)-1, 0, -1):
                if matrix[i]:
                    new_matrix.append(matrix[i].pop(0))
        return new_matrix


tests = [
    (
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         ),
        [1, 2, 3, 6, 9, 8, 7, 4, 5],
    ),
    (
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
         ),
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
    ),
    (
        ([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],
         ),
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ),
    (
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
         ),
        [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10],
    ),
]
