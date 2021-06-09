'''
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"

 

Constraints:

    1 <= s.length <= 10^5
    s[i] is one of  '(' , ')' and lowercase English letters.

'''
# "a)b(c)d" 
# stack = [1]

#res = [a, "", b, (, c, ), d]
def minRemoveToMakeValid(s: str): # 0(n) en tiempo y espacio
    stack, res = [], []
    for i in range(len(s)):
        res.append(s[i])
        if s[i] == '(':
            stack.append((i, '('))
        if stack:
            if stack[-1][1] == '(' and s[i] == ')':
                stack.pop()
            elif stack[-1][1] == ')' and s[i] == ')':
                stack.append((i, ')'))
        else:
            if s[i] == ')':
                stack.append((i, ')'))
            
    for par in stack:
        res[par[0]] = ''
        
    return ''.join(res)
        
    
print(minRemoveToMakeValid(")))))))))(((((((((("))




