"""
999. Available Captures for Rook

On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
In this example the rook is able to capture all the pawns.


Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation: 
Bishops are blocking the rook to capture any pawn.

Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
The rook can capture the pawns at positions b5, d6 and f5.

Solution:
This problem is trivial where we need to break it into two steps:
1. Loop through the board to find where the rook is.
2. From the rook's position: loop up, down, left, and right
	a. Check if there is a Bishop in the way
		i. If there is a bishop in the way then we break out of the loop and stop the loop here
	b. Check if there is a pawn in the way
		i. If there is a pawn we increment our result by 1 and break out of the loop
	c. Increment/Decrement the current index by 1
	d. Terminate the loop once we are out of bounds of the board.


numRookCaptures does part 1 and calls the helper
Helper method does part 2

O(m*n) runtime for the number of rows (m) and number of cols (n) 
It can also be argued O(1) if a chessboard input is always 8x8
"""
def helper(self, board, row, col):
        res = 0
        
        #look right
        col2 = col
        while col2 < len(board[0]):
            if board[row][col2] == 'B':
                break
            if board[row][col2] == 'p':
                res = res + 1
                break
            col2 = col2 + 1
        
        col2 = col
        while col2 > 0:
            if board[row][col2] == 'B':
                break
            if board[row][col2] == 'p':
                res = res + 1
                break
            col2 = col2 - 1
            
            
        row2 = row
        while row2 > 0:
            if board[row2][col] == 'B':
                break
            if board[row2][col] == 'p':
                res = res + 1
                break
            row2 = row2 - 1
        
        row2 = row
        while row2 < len(board):
            if board[row2][col] == 'B':
                break
            if board[row2][col] == 'p':
                res = res + 1
                break
            row2 = row2 + 1
        return res
        
        
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for row in range(len(board)):
            for col in range(len(board[row])):
                
                if board[row][col] == 'R':
                    return self.helper(board, row, col)
