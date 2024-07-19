'''
Code
Testcase
Testcase
Test Result
3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
Companies
Hint
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0 
        res = 0
        sub = set()
        for r in range(len(s)):
            while(s[r] in sub):
                sub.remove(s[l])
                l+=1
            sub.add(s[r])
            res = max(res , r -l +1)

        return res  
        