"""
994. Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

Solution:
Perform a bfs and keep track of the depth of each 'node' that gets added to the queue
Store the result in a variable and update it each time we see a larger depth.
Check if there are any remaining fresh oranges, if there is then we return -1 since it is not possible to rot these
Runtime: O(m*n)
Space: O(m*n)
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = []

        # Add the first rotted oranges to the queue with a depth of 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    queue.append({"coord": [row, col], "depth": 0})
                    
                    
        res = 0
        
        
        while len(queue) > 0:
            current_orange = queue.pop(0)
            current_row = current_orange["coord"][0]
            current_col = current_orange["coord"][1]
            depth = current_orange["depth"]
            
            res = max(res, depth)
            # check if in bounds and if the element is a fresh orange, we want to rot it then add it to the queue with a new depth
            
            if current_row - 1 >= 0 and grid[current_row - 1][current_col] == 1:
                grid[current_row - 1][current_col] = 2
                queue.append({"coord": [current_row - 1, current_col], "depth": depth + 1})
                
                
            if current_row + 1 <= len(grid) - 1 and grid[current_row + 1][current_col] == 1:
                grid[current_row + 1][current_col] = 2
                queue.append({"coord": [current_row + 1, current_col], "depth": depth + 1})
                
            
            if current_col - 1 >= 0 and grid[current_row][current_col - 1] == 1:
                grid[current_row][current_col - 1] = 2
                queue.append({"coord": [current_row, current_col - 1], "depth": depth + 1})
                
            if current_col + 1 <= len(grid[0]) - 1 and grid[current_row][current_col + 1] == 1:
                grid[current_row][current_col + 1] = 2
                queue.append({"coord": [current_row, current_col + 1], "depth": depth + 1})
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    return -1
        return res