'''189. Rotate Array
Solved
Medium
Topics
Companies
Hint
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k  = k % len(nums)

        l , r = 0 , len(nums)-1

        while(l<r):
            nums[l],nums[r] = nums[r] , nums[l]
            l+=1
            r-=1
        l , r = 0 , k -1

        while(l<r):
            nums[l],nums[r] = nums[r] , nums[l]
            l+=1
            r-=1

        l , r = k , len(nums)-1

        while(l<r):
            nums[l],nums[r] = nums[r] , nums[l]
            l+=1
            r-=1
            