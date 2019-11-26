"""
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Solution:
Start at the bottom left corner.
We need to compare the element at each step to the target.
1. If the element == target: return True
2. If the element >  target: the element is too big so we have to go smaller: move one row up
3. If the element <  target: the element is too small so we have to go bigger: move one col right
Runtime: O(m + n)
Space: O(N)
"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        row = len(matrix) - 1
        col = 0
        while True:
            if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
                return False
            
            
            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] > target:
                row = row - 1
            elif matrix[row][col] < target:
                col = col + 1
                
                
        
            