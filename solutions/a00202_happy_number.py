"""
Problem:
    202. Happy Number
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/happy-number
Tags:
    Hash Table, Math, Two Pointers
Date:
    2022-08-24T16:26:12.438715+08:00
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        nums = [n]
        while True:
            sum_of_square_digits = 0
            for c in str(n):
                sum_of_square_digits += int(c) ** 2
            n = sum_of_square_digits
            if sum_of_square_digits == 1:
                return True
            if sum_of_square_digits not in nums:
                nums.append(sum_of_square_digits)
            else:
                return False


tests = [
    (
        (19,
         ),
        True,
    ),
    (
        (2,
         ),
        False,
    ),
]
