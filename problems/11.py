"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


Solution:
The idea is to have two pointers one that starts from the beginning and one that starts at the end.
At each iteration we calculate the area and store it into a variable keeping track of the max area.
The area is calculated by the minimum height of the two pointers multiplied by the distance apart.
We are done with the loop once the left pointer crosses over the right pointer.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        start = 0
        end = len(height) - 1
        area = 0
        
        while start < end:
            temp = min(height[start], height[end]) * (end - start)
            area = max(area, temp)
            
            if height[start] > height[end]:
                end = end - 1
            else:
                start = start + 1
        return area
