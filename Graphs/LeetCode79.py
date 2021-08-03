'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


'''
class Solution:
    def dfs(self, board, i, j, k, word, visited):
        if k == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or visited[i][j] == 1 or word[k] != board[i][j]:
            return False
        
        visited[i][j] = 1
        res = self.dfs(board, i+1, j, k+1, word, visited) or self.dfs(board, i-1, j, k+1, word, visited) or self.dfs(board, i, j+1, k+1, word, visited) or self.dfs(board, i, j-1, k+1, word, visited)   
        visited[i][j] = 0
        return res
            
            
        
    def exist(self, board, word): # O(n^2) space ad and time
        visited = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, 0, word, visited):
                    return True
        return False
                
        