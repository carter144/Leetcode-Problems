"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Solution:
The O(N) solution is trivial. We can just scan the entire array until we find the target value and continue scanning until the find the last index of the target value.

Since this is a sorted input we can binary search for the target O(log N) and then do a linear scan to the left and right of that position.  This will cost us a total of O(log N + m) where N is the size of the input array and m is the number of occurences in the array

We can still do better with a O(log N) with using just binary search.  We will have to implement two binary search methods to find the starting index (left) and the ending index (right). 
"""

class Solution:
    
    
    def find_left(self, nums, target):
        
        
        lo = 0
        high = len(nums)
        
        while lo < high:
            mid = (lo + high) // 2
            
            if nums[mid] > target or target == nums[mid]:
                high = mid
            else:
                lo = mid + 1
        return lo
    
    def find_right(self, nums, target):
        lo = 0
        high = len(nums)
        
        while lo < high:
            mid = (lo + high) // 2
            if nums[mid] > target:
                high = mid
            else:
                lo = mid + 1
        return lo
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.find_left(nums, target)
        right = self.find_right(nums, target)
        
        
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        
        return [left, right - 1]