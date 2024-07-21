'''209. Minimum Size Subarray Sum
Solved
Medium
Topics
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:   
        #if sum(nums) < target : return 0
        s , l  = 0 , 0
       
        ln = float("inf")
        for r in range(len(nums)):

            s += nums[r]

            while s >= target:
                ln = min(ln , r-l+1)
                s -= nums[l]
                l +=1
                
            
        return 0 if ln == float("inf") else ln
        
        