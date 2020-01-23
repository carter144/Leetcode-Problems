"""
692. Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

Solution:

Have two hash maps and a heap
hash_map 1 will have the {word:frequency} as key value pairs
hash_map 2 will have the {frequency: word(s)} as key value pairs. The values are an array of words
Use a min heap to remove the least occuring frequencies

Runtime: O(N log K)
Space: O(N)

"""
class Solution:
    import heapq
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash_map = {}
        heap = []
        values_to_keys = {}
        for word in words:
            
            if word in hash_map:
                hash_map[word] += 1
            else:
                hash_map[word] = 1
                
        
        
        for key in hash_map.keys():
            val = hash_map[key]
            if val not in values_to_keys:
                values_to_keys[val] = []
            values_to_keys[val].append(key)
            
        
        for key in values_to_keys:
            heapq.heappush(heap, key)
            
            if len(heap) > k:
                heapq.heappop(heap)
                
        heap = sorted(heap)[::-1]
       
        res = []
        for val in heap:
            arr = sorted(values_to_keys[val])
            
            for i in range(len(arr)):
                if len(res) < k:
                    res.append(arr[i])
        return res