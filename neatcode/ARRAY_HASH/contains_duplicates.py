'''

Duplicate Integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

'''


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            if nums.count(i)>=2:
                return True
        return False