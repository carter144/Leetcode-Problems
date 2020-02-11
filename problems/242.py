"""
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

Solution:
Have two dictionaries that store the strings s and t letter's and their occurances
Loop through the dictionaries keys and see if they match values
If there is no match then we return false
Runtime: O(N)
Space: O(N)
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        
        
        
        for letter in s:
            if letter not in dict1:
                dict1[letter] = 1
            else:
                dict1[letter] += 1
        
        
        for letter in t:
            if letter not in dict2:
                dict2[letter] = 1
            else:
                dict2[letter] += 1
        
        
        
        for key in dict1.keys():
            
            
            if key not in dict2 or dict1[key] != dict2[key]:
                return False
        
        
        
        for key in dict2.keys():
            if key not in dict1 or dict2[key] != dict1[key]:
                return False
            
        return True