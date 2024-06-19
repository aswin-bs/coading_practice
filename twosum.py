'''
Two Integer Sum
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
'''

class Solution:
    def      twoSum(self, nums: List[int], target: int) -> List[int]:
        dmap = {}

        for i , n in enumerate(nums):
            diff  = target-n
            if diff in dmap:
                return [dmap[diff],i]
            dmap[n]=i   