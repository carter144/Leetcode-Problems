"""
59. Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

Solution:
This is very similar to Spiral Matrix (problem 54).
The thing we change is that we are populating a 2d array with values. We just have to keep a counter an increment by one each time in a for loop.

1. Keep boundaries of rowBegin, rowEnd, colBegin, colEnd

2. Traverse the 2d matrix and place values of counter that increments
	2a. Move right
	2b. Move Down
	2c. Move Left
	2d. Move up
3. Reset boundaries and repeat

Runtime: O(N^2)
Space: O(N^2)
"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for x in range(n)] for y in range(n)]
        
        
        if len(matrix) == 0:
            return []
        
        #boundaries for looping
        rowBegin = 0
        rowEnd = len(matrix) - 1
        
        colBegin = 0
        colEnd = len(matrix[0]) - 1
        
        res = []
        counter = 1
        
        while rowBegin <= rowEnd and colBegin <= colEnd:
            
            
            # Loop the columns (MOVING RIGHT)
            for i in range(colBegin, colEnd + 1):
                matrix[rowBegin][i] = counter
                counter += 1

            # We processed the first row, so we move down
            rowBegin += 1
            
            # Loop through the rows (MOVING DOWN)
            for i in range(rowBegin, rowEnd + 1):
                matrix[i][colEnd] = counter
                counter += 1

            # We processed the end column we move inwards 
            colEnd -= 1
            
            # IF there are items still to be processed
            if rowBegin <= rowEnd:
                
                # We loop through the columns backwards (MOVING LEFT)
                for i in range(colEnd, colBegin - 1, -1):
                    matrix[rowEnd][i] = counter
                    counter += 1
                    
            # We processed the last row so we move up
            rowEnd -= 1
            
            # If there are item still to be processed
            if colBegin <= colEnd:
                
                # We loop through the rows backwards (MOVING UP)
                for i in range(rowEnd, rowBegin - 1, -1):
                    matrix[i][colBegin] = counter
                    counter += 1
                    
            # We processed the left column so we move inwards to the right 1        
            colBegin += 1
        return matrix
        
        
