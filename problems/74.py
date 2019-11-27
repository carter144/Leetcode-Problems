"""
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

Solution:
Perform a binary search.
Left = 0
Right = (m * n) - 1

To calculate row: row = mid // n where n is the number of columns
To calculate col: col = mid %  n where n is the number of columns


Then do a normal binary search
Runtime: O(log(m*n))
Space: O(1)

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        if len(matrix) == 0:
            return False
        
        right = (len(matrix) * len(matrix[0])) - 1
        
        
        while left <= right:
            mid = (left + right) // 2
            
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
            
            
        return False