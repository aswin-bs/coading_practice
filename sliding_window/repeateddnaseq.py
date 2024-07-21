'''
Code
Testcase
Testcase
Test Result
187. Repeated DNA Sequences
Solved
Medium
Topics
Companies
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
'''

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l = 0
        array = []
        
        for r in range(9 , len(s)):

            if s[l:r+1] in s[l+1:len(s)]:
                
                if s[l:r+1] not in array : array.append(s[l:r+1])
            l+=1

        return array    
    
#more efficient
'''        seen , res = set() , set()

        for l in range(len(s) - 9):
            cur = s[l:l+10]
            if cur in seen:
                res.add(cur)
            seen.add(cur)
        return list(res)'''