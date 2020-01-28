"""
215. Kth Largest Element in an Array


Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

Solution:
Use a min heap to find the kth largest element.
We add items from the array into the min heap. Once the size of the heap gets above K,
we need to start popping elements off the heap, this will remove the smallest elements first.
At the end we are left with the kth largest element at the top of the heap.

Runtime: O(N log k)
Space: O(K)
"""
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for i in nums:
            heapq.heappush(heap, i)
            
            
            if len(heap) > k:
                heapq.heappop(heap)
                
        return heap[0]
