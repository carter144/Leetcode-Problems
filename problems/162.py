"""
162. Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.

Solution:
If we think of this as a graph plotted on a line then we can see that there are rising slopes and decreasing slopes.
We use binary search to reduce the search space:
1. If we land on a rising slope then we know the peak element is to the right
2. If we land on a decreasing slope then we know the peak element is to the left
So we reduce our search space to the left or right each time
Runtime: O(log n)
Space: O(log n)
"""
class Solution:
    
    def binarySearch(self, nums, left, right):
        mid = (left + right) // 2
        if left == right:
            return left
        if nums[mid] > nums[mid + 1]:
            return self.binarySearch(nums, left, mid)
        return self.binarySearch(nums, mid + 1, right)
        
    def findPeakElement(self, nums: List[int]) -> int:
        
        return self.binarySearch(nums, 0, len(nums) - 1)
        # binary search until nums[index - 1] < nums[index] and nums[index + 1] > nums[index]