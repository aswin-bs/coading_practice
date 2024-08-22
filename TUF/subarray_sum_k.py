class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dict_prefix = {0:1}
        count , prefix_sum = 0 , 0

        for  i in range(len(nums)):

            prefix_sum += nums[i]

            if prefix_sum - k in dict_prefix:
                
                count += dict_prefix[prefix_sum - k]

            if prefix_sum in dict_prefix:
                dict_prefix[prefix_sum ] += 1
            else:
                dict_prefix[prefix_sum ] = 1

        return count