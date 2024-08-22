class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        s = n*(n+1)//2

        return s - sum(nums) 

       
'''
Code


Testcase
Testcase
Test Result
268. Missing Number
Solved
Easy
Topics
Companies
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.'''