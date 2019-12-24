"""
1296. Divide Array in Sets of K Consecutive Numbers

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [3,3,2,2,1,1], k = 3
Output: true
Example 4:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.

Solution:
A brute force solution would be to partition the array into buckets. In the first example we would have two buckets.
Then we would greedily populate each bucket with distinct minimum values from a sorted array. If we are unable to fill the two buckets we would return false.
At the end we would check each bucket to make sure the elements are increasing by 1. This solution will have TLE.

Another solution is to use a heap and a hash map. The heap will always have the minimum element at the top and the hash map will count how many times a value occur in the array. We loop until the heap is empty and pop the minimum value. Then we look from 1 to k and check if the next element difference is greater than 1. If it is we will return false. We will also return false if there are no items to pop off the heap.

After the loop has completed we will return True if we didn't already return false previously.

Runtime: O(N Log N)
Space: O(N)
"""
class Solution:
    import heapq
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        # Check if it is possible by doing math
        if len(nums) % k != 0:
            return False
        # Initialize a hash map and a heap
        hash_map = {}
        heap = []
        
        # Populate the hash_map thius will store the frequencies of each number
        for item in nums:
            if item not in hash_map:
                hash_map[item] = 1
            else:
                hash_map[item] += 1
            
        # Populate the heap with the keys of the hash_map
        for key in hash_map.keys():
            heapq.heappush(heap, key)
            
            
       # Loop until the heap is empty
        while len(heap) > 0:
            # create a temporary array to hold elements we've seen
            holding = []
            
            # Grab the minimum value and remove it from the heap
            top_elem = heapq.heappop(heap)
            
            # temporarily hold that value
            holding.append(top_elem)
            
            # loop until we reached k
            for i in range(1, k):
                
                # If the heap is empty and we can't pop anything, return false
                if len(heap) <= 0:
                    return False
                # Pop the next smallest element from the heap
                second_top_elem = heapq.heappop(heap)
                
                # check if the difference is more than 1, if so return false
                if abs(top_elem - second_top_elem) > 1:
                    return False
                
                # Add the element we just popped to the temporary array
                holding.append(second_top_elem)
                
                # the new smallest element will be the second_top_elem
                top_elem = second_top_elem
            
            # we have to add items back to the heap by checking the count of each element
            for number in holding:
                if hash_map[number] - 1 > 0:
                    heapq.heappush(heap, number)
                # we also have to decrease the count because we just used the element above
                hash_map[number] -= 1
        
        return True