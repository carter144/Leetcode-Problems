"""
347. Top K Frequent Elements


Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

Soution:
Use two hash_maps and a heap.
1. hash_map will contain key, value pairs for each element in num and their frequencies.
2. hash_map2 will contain key, value pairs of frequencies as keys and values are arrays of elements
3. To retrieve the highest keys from hash_map2 we use a min heap to store the highest numbers while we evict lowest numbers
4. We need to sort the heap and then reverse it to get the highest value
5. Retrieve the list with the highest values in the heap by using hash_map2 and add elements to the result array.
"""
class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        hash_map = {}
        res = []
        hash_map2 = {}
        for elem in nums:
            if elem in hash_map:
                hash_map[elem] += 1
            else:
                hash_map[elem] = 1
                
                
        
        for key in hash_map.keys():
            value = hash_map[key]
            if value not in hash_map2:
                hash_map2[value] = []
            hash_map2[value].append(key)
            
            
        for key in hash_map2.keys():
            heapq.heappush(heap, key)
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        v = sorted(heap)[::-1]

        for item in v:
            for elem in hash_map2[item]:
                if len(res) < k:
                    res.append(elem)
        return res