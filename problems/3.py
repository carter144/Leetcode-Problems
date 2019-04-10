"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.\


Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


Solution:
Loop through each letter in the string and have a sliding window with two pointers.
Place the letters in the window into a set
On the next iteration if the letter at the end of the window exists in our set then we increment our start position of our window
If the letter doesn't exist in the set, then we increment the end pointer and place the letter into the set

During the process we keep track of the max size of the set.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        begin = 0
        end = 0
        
        temp_set = set()
        while end < len(s) and begin < len(s):
        
            if s[end] not in temp_set:
                temp_set.add(s[end])
                
                res = max(res, len(temp_set))
                end = end + 1
                
            else:
                
                temp_set.remove(s[begin])
                begin = begin + 1
        return res
