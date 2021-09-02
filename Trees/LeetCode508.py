'''
Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).
Example 1:
       5
      / \
     2   -3
     
Input: root = [5,2,-3]
Output: [2,-3,4]

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def __init__(self):
        self.map = {}
    # PostOrder travelsal, compute sum from leaves to root    
        
    def compute_map(self, node):
        if not node:
            return
        self.compute_map(node.left)
        self.compute_map(node.right)
        
        self.map[node] = node.val
        if node.left in self.map:
            self.map[node] += self.map[node.left]
        if node.right in self.map:
            self.map[node] += self.map[node.right]
            
    def findFrequentTreeSum(self, root):
        self.compute_map(root) # Computer sum from all nodes
        sum_counter = Counter(self.map.values()) # Get count of the values
        most_freq_sum = max(sum_counter.values()) # Get the most freq sum

        res = []
        for sums in sum_counter: 
            if sum_counter[sums] == most_freq_sum:
                res.append(sums)
        return res
        