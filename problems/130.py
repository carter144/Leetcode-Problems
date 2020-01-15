"""
130. Surrounded Regions


Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Solution:
Search the outer boundaries for the O's that cannot be turned into X's
Once we find an O on the outer boundary we perform a DFS to turn all of these O's to *'s
At the end, we turn all remaining O's to X's and turn back *'s into O's

Runtime: O(MN)
Space: O(MN)
"""



class Solution:
    
    def dfs(self, board, row, col):
        
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return
        
        
        if board[row][col] == "O":
            board[row][col] = "*"
            
        
        if row > 0 and board[row - 1][col] == "O":
            self.dfs(board, row - 1, col)
            
            
        
        if col > 0 and board[row][col - 1] == "O":
            self.dfs(board, row, col - 1)
            
        if row < len(board) - 1 and board[row + 1][col] == "O":
            self.dfs(board, row + 1, col)
            
        if col < len(board[0]) - 1 and board[row][col + 1] == "O":
            self.dfs(board, row, col + 1)
        return
        
            
        
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return board
        
        
        rows = len(board)
        cols = len(board[0])
        
        
        for i in range(rows):
            if board[i][0] == "O":
                self.dfs(board, i, 0)
            
            if board[i][cols - 1] == "O":
                self.dfs(board, i, cols -  1)
                
        for j in range(cols):
            if board[0][j] == "O":
                self.dfs(board, 0, j)
                
            if board[rows - 1][j] == "O":
                self.dfs(board, rows - 1, j)
        
        
        for row in range(rows):
            for col in range(cols):
                
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "*":
                    board[row][col] = "O"
                    
                    
        return board