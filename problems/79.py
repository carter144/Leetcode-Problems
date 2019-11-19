"""
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

Solution:
Loop through each element in the 2D grid.
When we see the first letter of the word we perform a DFS to search for the other letters within the word. We have to create a visited 2D array to keep track of what elements have been visited.

Runtime: O(M*(N^2))
Space: O(M*N)
"""
class Solution:
    
    
    def helper(self, board, row, col, visited, word, index):

    	# Bounds check
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[row]) or index >= len(word):
            return False
        # If we already visited it
        if (visited[row][col]):
            return False
        # If the letter does not equal the word's letter
        if board[row][col] != word[index]:
            return False
        # If we end up past the word
        if (index == len(word) - 1):
            return True
        

        
        # mark the current cell visited to true
        visited[row][col] = True
        

        
        k = (self.helper(board, row + 1, col, visited, word, index + 1) or
        self.helper(board, row - 1, col, visited, word, index + 1) or
        self.helper(board, row, col + 1, visited, word, index + 1) or
        self.helper(board, row, col - 1, visited, word, index + 1))
        
        if (k):
            return True
        visited[row][col] = False
        return False
       
        
        
        
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word is None:
            return False
        if len(word) == 0:
            return False
        m = len(board)
        n = len(board[m - 1])
        #visited = [[False for x in range(n)] for y in range(m)] 
        
        
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    visited = [[False for x in range(n)] for y in range(m)]
                    
                    if self.helper(board, row, col, visited, word, 0):
                        return True
        return False