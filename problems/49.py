"""
49. Group Anagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

Solution:

1. Loop through every element on the string and store it into hash_map/dictionary
2. Keys will be the sorted string, and values will be a list of unsorted strings
3. Iterate through the hash_map and add each value into the result array.
Runtime O(N * (M log M)) where N is the length of the list and M is the longest string
Space O(N) for hash_map

"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    	# Initialize a hash_map
        hash_map = {}
        
        # Loop through each item
        for item in strs:
            
            # The key is the sorted string
            key = ''.join(sorted(item))

            # if the key already exists, add it to that bucket
            if key in hash_map:
                hash_map[key].append(item)

            # otherwise create a bucket for that key and add the item
            else:
                hash_map[key] = []
                hash_map[key].append(item)
        res = []
        
        
        for key in hash_map.keys():
            res.append(hash_map[key])
            
        return res

