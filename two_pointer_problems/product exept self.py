'''
Code
Testcase
Testcase
Test Result
238. Product of Array Except Self
Solved
Medium
Topics
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):

            res[i] = prefix
            prefix *= nums[i] 

        postfix = 1
        for i in range(len(nums)-1, -1 , -1):
            res[i] *= postfix
            postfix *= nums[i] 

        return res
