"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Solution:
First we want to initialize a hash map to map the digits to the corresponding letters.
Next we have a recursive function that builds out our result.
The recursive function performs a dfs and keeps adding all possiblle combinations of letters until we reach the base case which is when the index >= len(digits)
"""

class Solution:
    
    def helper(self, digits, index, hash_map, current, res):
        if index >= len(digits):
            res.append(current)
            return
        
        if digits[index] not in hash_map:
            self.helper(digits, index + 1, hash_map, current, res)
            
            
        current_digit = digits[index]
        
        for i in (hash_map[current_digit]):
            self.helper(digits, index + 1, hash_map, current + [i], res)
        
        
        
        
    def letterCombinations(self, digits: str) -> List[str]:
        hash_map = {"2": ['a', 'b', 'c'],
                   "3": ['d', 'e', 'f'],
                   "4": ['g', 'h', 'i'],
                   "5": ['j', 'k', 'l'],
                   "6": ['m', 'n', 'o'],
                   "7": ['p', 'q', 'r', 's'],
                   "8": ['t', 'u', 'v'],
                   "9": ['w', 'x', 'y', 'z']}
        
        res = []
        res2 = []
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return hash_map[digits]
        
        self.helper(list(digits), 0, hash_map, [], res)
        for word in res:
            res2.append(''.join(word))
        return res2