"""
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Solution:
1. Find the pivot index
	1a. look at the last element of the array
	2b. Conduct a binary search to find the pivot index
2. If the pivot index is 0: do a normal binary search
3. Do a binary search from everything to left up to pivot index.
4. If there is no result then do a binary search from every to the right of the pivot index

Runtime: O(log N)
Space: O(1)
"""
class Solution:
    
    def findPivotIndex(self, nums):
        low = 0
        high = len(nums) - 1
        end_elem = nums[high]
        
        
        while low < high:
            mid = (low + high) // 2
            if mid + 1 <= len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return mid + 1

            # [4,5,6,7,0,1,2]
            #        ^ --- ^
            # we need to move low to the right
            elif nums[mid] > end_elem:
                low = mid
            # [8,0,1,2,3,4,5,6,7]
            #  ---     ^       ^
            # we need to move high to the right
            elif nums[mid] < end_elem:
                high = mid
        
        if nums[low] < nums[low + 1]:
            return low
        if nums[high] < nums[high - 1]:
            return high
        
        return -1
        
        
    def binarySearch(self, nums, target, start, end):
        
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        return -1
    
    
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
            
            
            
        
            
        pivotIndex = self.findPivotIndex(nums)
        if target == nums[pivotIndex]:
            return pivotIndex
        if pivotIndex == 0:
            return self.binarySearch(nums, target, 0, len(nums) - 1)
        res = -1
        
        res = self.binarySearch(nums, target, 0, pivotIndex)
        if res == -1:
            res = self.binarySearch(nums, target, pivotIndex, len(nums) - 1)
        
        
        return res
