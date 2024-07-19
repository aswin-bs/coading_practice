'''
Code
Testcase
Testcase
Test Result
1838. Frequency of the Most Frequent Element
Solved
Medium
Topics
Companies
Hint
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

 '''

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        total = 0
        l , r = 0 , 0
        res = 0

        while r<len(nums):
            total = total + nums[r]
            while nums[r]*(r-l+1) > total + k:
                total = total - nums[l]
                l +=1

            res = max(res , r-l+1)
            r+=1

        return res



        