"""
26. Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

Solution:
A trivial solution is to loop through the array with index i. Then at each element after that we check if the element is equal to the element at index i. If they are equal we replace it with None.  Then we remove all the None elements from the array.

O(N) runtime
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        
        while i < len(nums):
            current = nums[i]
            j = i + 1
            
            if j < len(nums):
                
                while j < len(nums) and nums[j] == current:
                    nums[j] = None
                    j = j + 1
            i = j
        while None in nums:
            nums.remove(None)
                
        return len(nums)
