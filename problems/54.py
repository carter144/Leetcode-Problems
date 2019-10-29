"""
54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Solution:
Keep starting and ending boundaries for the rows and columns.
Runtime: O(m*n)
Space: O(m*n) for result array, otherwise O(1)

"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix) == 0:
            return []
        
        #boundaries for looping
        rowBegin = 0
        rowEnd = len(matrix) - 1
        
        colBegin = 0
        colEnd = len(matrix[0]) - 1
        
        res = []
        
        
        while rowBegin <= rowEnd and colBegin <= colEnd:
            
            
            # Loop the columns (MOVING RIGHT)
            for i in range(colBegin, colEnd + 1):
                res.append(matrix[rowBegin][i])
            
            # We processed the first row, so we move down
            rowBegin += 1
            
            # Loop through the rows (MOVING DOWN)
            for i in range(rowBegin, rowEnd + 1):
                res.append(matrix[i][colEnd])
            
            # We processed the end column we move inwards 
            colEnd -= 1
            
            # IF there are items still to be processed
            if rowBegin <= rowEnd:
                
                # We loop through the columns backwards (MOVING LEFT)
                for i in range(colEnd, colBegin - 1, -1):
                    res.append(matrix[rowEnd][i])
                    
            # We processed the last row so we move up
            rowEnd -= 1
            
            # If there are item still to be processed
            if colBegin <= colEnd:
                
                # We loop through the rows backwards (MOVING UP)
                for i in range(rowEnd, rowBegin - 1, -1):
                    res.append(matrix[i][colBegin])
                    
            # We processed the left column so we move inwards to the right 1        
            colBegin += 1
        return res