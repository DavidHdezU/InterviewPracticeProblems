'''
Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

 

Example 1:

Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).

Example 2:

Input: s = "abc", cost = [1,2,3]
Output: 0
Explanation: You don't need to delete any character because there are no identical letters next to each other.

Example 3:

Input: s = "aabaa", cost = [1,2,3,4,1]
Output: 2
Explanation: Delete the first and the last character, getting the string ("aba").

 

Constraints:

    s.length == cost.length
    1 <= s.length, cost.length <= 10^5
    1 <= cost[i] <= 10^4
    s contains only lowercase English letters.


'''
import numpy as np
import random
import time
import string

def minCost1(s, cost):
    start, end = 0, 1
    min_value = float('inf')
    curr_sum = 0
    flag = False

    while end < len(cost): 
        if s[end] == s[start]:
            flag = True
            min_value = min(cost[end], cost[start])
            curr_sum += min_value
              
            if cost[end] < cost[start]:
                end += 1
            else:
                if flag:
                    end += 1
                    start = end -1
                else:
                    end += 1
                    start += 1
                

        else:
            if flag:
                start = end - 1
            end += 1
            start += 1

    return curr_sum

def minCost2(s, cost):
    left = 0
    curr_min = 0
        
    for i in range(1, len(s)):
        if s[i] == s[left]:
            if cost[left] <= cost[i]:  # When the left char has a lower cost, it means we don't have to search for the next greatest cost
                curr_min += cost[left]
                left = i
            else:
                curr_min += cost[i] # The right char has a lower cost, so we have to search the next greatest cost
                    
        else:
            left = i    
    return curr_min

s = ""
for i in range(1000000):
    s += random.choice(string.ascii_lowercase)
        
cost = np.random.randint(low=1,high=10, size=1000000)



start_time1 = time.time()
print(minCost1(s, cost))
end_time1 = time.time() - start_time1

start_time2 = time.time()
print(minCost2(s, cost))
end_time2 = time.time() - start_time2


print("--- %s seconds ---" % (end_time1))
print("--- %s seconds ---" % (end_time2))


