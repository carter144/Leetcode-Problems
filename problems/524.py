"""
524. Longest Word in Dictionary through Deleting

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.

Solution:
Loop through the words in d
Check if the word is a subsequence of s
If it is then we update the result only if it meets the criteria.
Runtime: O(N*X) N is number of strings and X is the length
Space: O(X)
"""
class Solution:
    
    def isSubSequence(self, str1, str2):
        i = 0
        j = 0
        
        while j < len(str2) and i < len(str1):
            if str2[j] == str1[i]:
                i+= 1
            j += 1
        return i == len(str1)
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = ""
    
        for word in d:
            if (self.isSubSequence(word, s)):
                if (len(word) > len(res)) or (len(word) == len(res) and word < res):
                    res = word
        return res