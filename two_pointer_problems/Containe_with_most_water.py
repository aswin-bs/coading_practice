'''
Code
Testcase
Testcase
Test Result
11. Container With Most Water
Solved
Medium
Topics
Companies
Hint
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        res =  0 
        l , r = 0 , len(height) - 1

        while (l<r):
            
            n = min(height[l] , height[r]) * (r-l)
            print(n)
            res = max(res,n)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return res