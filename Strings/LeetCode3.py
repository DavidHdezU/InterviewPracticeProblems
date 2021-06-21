'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces
'''
def count_char(i, s, seen):   #a  b  c  a  b  c
    count = 0                 #
    for j in range(i, len(s)):
        if s[j] in seen:
            break
        seen.add(s[j])
        count += 1
        
    seen.clear()
    return count
    
def lengthOfLongestSubstring(s: str):
    count = 1
    i = 0
    seen = set()
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            count = max(count, count_char(i, s, seen))
        
    return count
            
        
        
print(lengthOfLongestSubstring("pwwkew"))