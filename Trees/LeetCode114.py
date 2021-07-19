'''
Given the root of a binary tree, flatten the tree into a "linked list":

    The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
    The "linked list" should be in the same order as a pre-order traversal of the binary tree.

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def helper(self, node): # Post Order 
        if not node:
            return
        
        self.helper(node.right)
        self.helper(node.left)
        
        node.right = self.prev # Cambiamos la referencia al previo
        node.left = None       # Como el previo siempre es primero el derecho al hacer recursión en el izquierdo, referenciamos bien
        self.prev = node

    def flatten(self, root): # Preorder -> O(n) espacio O(n) tiempo
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        res = []
        
        while stack:
            curr = stack.pop()
            res.append(curr)
            
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
                
        for i in range(len(res)-1): # Sólo reasignamos los derechos
            curr_node = res[i]
            curr_node.right = res[i+1]
            curr_node.left = None 
        
    def flatten(self, root): # Recursivo O(n) espacio O(n) tiempo
        self.prev = None
        self.helper(root)
            
        
        
        