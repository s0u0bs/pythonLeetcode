"""
Problem:
    27. Remove Element
Difficulty:
    Easy
URL:
    https://leetcode.com/problems/remove-element
Tags:
    Array, Two Pointers
Date:
    2022-05-10T14:00:29.877163+08:00
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


tests = [
    (
        ([3, 2, 2, 3], 3,
         ),
        2,
    ),
    (
        ([0, 1, 2, 2, 3, 0, 4, 2], 2,
         ),
        5,
    ),
]
