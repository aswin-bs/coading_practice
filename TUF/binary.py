class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        

        def binarysearch(nums , target , flag_left):

            l , h = 0 , len(nums) - 1

            idx = -1

            while l <= h :

                mid = l + (h-l)//2

                if nums[mid] == target:

                    if flag_left:
                        idx = mid 
                        h = mid-1
                    else:
                        idx = mid
                        l = mid+1

                if nums[mid] < target :

                    l = mid + 1
                if nums[mid] > target:
                    h = mid - 1

            return idx

        left = binarysearch(nums , target , True)
        right = binarysearch(nums , target , False)

        return [left , right]