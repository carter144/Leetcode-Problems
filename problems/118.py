"""
118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Solution:
Initialize an array with the first two rows: it will always be [1], [1, 1]
Loop from 2 to the numRows
Create a new array and add 1 to it since we always know each row starts with 1
Grab the previous row and loop through the elements of that and sum up adjacent numbers and append to the new array
After the loop, add 1 to the array and append the array to result.
Rutime: O(N^2)
Space: O(N^2)
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1], [1, 1]]
        
        
        res = [[1], [1, 1]]
        
        for i in range(2, numRows):
            
            temp = [1]
            
            for j in range(0, len(res[i - 1]) - 1):
                temp_sum = res[i - 1][j + 1] + res[i - 1][j]
                temp.append(temp_sum)
            
            
            temp.append(1)
            res.append(temp)
            
            
        return res