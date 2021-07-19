'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
'''
class Solution:
    def is_pal(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
                
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""
        
        start, end = 0, 0
        sl, sr, max_len = 0, 0, 0
        while end < len(s):
            if self.is_pal(s[start:end+1]):
                if len(s[start:end+1]) > max_len:
                    sl = start
                    sr = end
                    max_len = len(s[start:end+1])
                end += 1
            else: 
                aux_end = end
                while s[start] != s[aux_end] and aux_end < len(s)-1:
                    print(aux_end)
                    aux_end += 1
                
                if s[start] == s[aux_end]:
                    if self.is_pal(s[start:aux_end+1]):
                        sl = start
                        sr = aux_end
                        end = aux_end
                    else:
                        start = end
                else:
                    start =  end
                        
                            
        return s[sl:sr+1]
    
    
test = "babad"
sol = Solution()
print(sol.longestPalindrome(test))