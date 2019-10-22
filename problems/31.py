"""
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

Solution:
1. Start from the end of the array and loop backwards until we find an element to the right that is bigger. (INDEX i)
2. Start another loop from the end of the array and loop backwards until we find an element that is bigger than the element at index i. (INDEX j)
3. Swap the two elements at index i and index j.
4. Reverse everything from index i + 1 to the end of the array

Runtime: O(N)
Space: O(1)
"""
class Solution:
    
    def reverse(self, nums, start, end):
        
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            
            end -= 1
            start += 1
        
        
        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # second to last element in array
        i = len(nums) - 2
        
        # walk backwards until we find the element to the right is bigger and we stop there
        
        # [6, 2, 1, 5, 3, 2, 0]
        #                 i
        #              i
        #           i
        #        i
        while i >= 0 and nums[i] >= nums[i + 1]:
            i = i - 1
            
        if i >= 0:
            
            j = len(nums) - 1
            #start at end of array and search for the first number that is greater than nums[i]
            # [6, 2, 1, 5, 3, 2, 0]
            #        i           j
            #        i        j
            #        i     
            #        i 
            while j >= 0 and nums[i] >= nums[j]:
                j = j - 1
            
            # swap the two elements
            
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            
            # [6, 2, 1, 5, 3, 2, 0]
            #        ^        ^
            
            # [6, 2, 2, 5, 3, 1, 0]
            #        ^        ^
            
            
            self.reverse(nums, i + 1, len(nums) - 1)
            # Reverse everything after the position i
            # [6, 2, 2, 5, 3, 1, 0]
            #           ----------
            
            # [6, 2, 2, 0, 1, 3, 5]
            #           ----------
            
        else:
            self.reverse(nums, 0, len(nums) - 1)