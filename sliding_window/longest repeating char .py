'''424. Longest Repeating Character Replacement
Solved
Medium
Topics
Companies
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        l= 0
        maxfreq = 0
        res = 0

        for r in range(len(s)):

            count[s[r]] = 1 + count.get(s[r],0)

            maxfreq = max(maxfreq , s[r])

            while (r-l+1) - maxfreq > k:
                count[l] -=1
                l = l+ 1

            res = max(res , r-l+1)

        return res
