#### Little tricks and strategies I have found for tree problems

## Find subtrees
1. When we are asked to asked any subtree we're going to need to traverse the tree in some way, usually I have found the most common technique is to used a Preorder traversal, i.e, visiting the left and right subtree first and then the root

2. Also it's going to be useful sometimes to use a HashMap or HashSet

A example of this is LeetCode 652

```
https://leetcode.com/problems/find-duplicate-subtrees/
```