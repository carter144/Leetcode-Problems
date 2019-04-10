"""
4. Median of sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5


Solution:

We will have to partition the arrays a and b in half into a total of 4 subarrays. We will end up with:

1. Left half of A: leftA
2. Right half of A: rightA
3. Left half of B: leftB
4. Right half of B: rightB


We keep will keep partitioning until we satisfy the following two conditions:

1. The maximum element in leftA has to be less than or equal to the minimum element in rightB
2. The minimum element in rightB has to be greather than or equal to the maximum element in leftA


To partition A and B we can use binary search method to figure out where to partition A. Then for B
We take the sum of the lengths (m + n + 1) / 2 and subtract the partition of A


Then if the two conditions are not met above then we binary search we have two cases:
1. The maximum element in leftA is greather than the minimum element in rightB we went too high so we set high to partitionA - 1
2. THe two conditions doesn't meet (Else): we went too low so we set low = partitionA + 1

"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
            
        low = 0
        high = len(nums1)
        
        
        
        while low <= high:
            partitionA = (low + high) // 2
            partitionB = (len(nums1) + len(nums2) + 1) // 2 - partitionA
            
            
            if partitionA > 0:
                maxLeftA = nums1[partitionA - 1]
            else:
                maxLeftA = float('-inf')
                
            if partitionB > 0:
                maxLeftB = nums2[partitionB - 1]
            else:
                maxLeftB = float('-inf')
                
                
            if partitionA == len(nums1):
                minRightA = float('inf') 
            else:
                minRightA = nums1[partitionA]
                
            
            if partitionB == len(nums2):
                minRightB = float('inf')
            else:
                minRightB = nums2[partitionB]
                
                
            if maxLeftA <= minRightB and minRightA >= maxLeftB:
                if ((len(nums1) + len(nums2)) % 2 == 0):
                    return float((max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2.0)
                else:
                    return float(max(maxLeftA, maxLeftB))
            elif maxLeftA > minRightB:
                high = partitionA - 1
            else:
                low = partitionA + 1