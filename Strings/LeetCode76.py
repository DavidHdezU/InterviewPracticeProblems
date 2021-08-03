'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
'''
from collections import Counter
import math
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if s == t:
            return s
        
        t_chars = Counter(t)  # O(t)   
        counter = {} # O(t)
        start, end = 0, 0
        i, j = 0, math.inf
        chars = 0
        while end < len(s): # O(s)
            curr_char = s[end]
            if curr_char in t_chars:
                counter[curr_char] = counter.get(curr_char, 0) + 1
            
            if curr_char in t_chars:
                if counter[curr_char] == t_chars[curr_char]:
                    chars += 1
            
            while start <= end and chars == len(t_chars):
                if end-start + 1 < j-i:
                    i = start
                    j = end
                    
                start_char = s[start]
                if start_char in t_chars:
                    counter[start_char] -= 1
                
                if start_char in t_chars and counter[start_char] < t_chars[start_char]:
                    chars -= 1
                    
                start += 1
            end += 1
            
        if j != math.inf:
            return s[i:j+1]
        return ""

                
s = "ADOBECODEBANC"
t = "ABC"

sol = Solution()
print(sol.minWindow(s, t))
                
                    
                            
                        
                    
            
                