"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Solution:
Take the first word and loop through each letter of the first word.
Check each of the remaining words and see if they have the same letter.
return once we are out of bounds with index or the letter doesn't match.

O(m*n) where m is the length of shortest word and n is the size of the strs
O(1) space since we are not using any extra space
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # edge cases
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        # Grab the first word
        first_word = strs[0]
        index = 0

        # Initialize a result array 
        res = []
        
        # loop through each letter in the first word
        while index < len(first_word):
            
            # loop through the remaining words
            for i in range(1, len(strs)):
                word = strs[i]
                
                # if the index is out of bounds OR the letters don't match we return
                if index >= len(word) or word[index] != first_word[index]:
                    return ''.join(res)
                
            # add the letter to the result array if they match
            res.append(first_word[index])
            # increment index to look at the next letter
            index += 1
        return ''.join(res)