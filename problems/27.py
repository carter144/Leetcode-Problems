"""
27. Remove Element
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.

Solution:

We have two variables: i and j. variable j will be the fast and variable i will be the slow.  We use a for loop with the variable j to iterate through each element.  If the item at index j is not the value: then we copy that value to where i is currently pointing and increment i.  If the value is equal to the item at index j then we continue in our loop and keep i at its current location

Runtime O(N)
Space: O(1) 
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i