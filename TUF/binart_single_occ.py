#Single non duplicate elemet in logn

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        if len(nums) == 1 : return nums[0]

        if nums[len(nums)-1] != nums[len(nums)-2] : return nums[len(nums)-1]
        l , r  = 0 , len(nums) - 1

        while(l<=r):

            

            mid = l + (r-l)//2

            if mid%2 == 1 and mid != 0:
                mid = mid -1
            
            if nums[mid -1] != nums[mid] and nums[mid] != nums[mid+1]:
                return nums[mid]

            if nums[mid-1] == nums[mid]:
                r = mid -1
            else:
                l = mid + 1




        
        