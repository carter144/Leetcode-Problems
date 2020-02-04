"""
243. Shortest Word Distance

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

Solution:
Have two variables that keep track of the indexes of each word: index_1 and index_2
Update the index of the variable once we reach that word
Calculate the result by taking the min and absolute difference between each index

Runtime: O(N)
Space: O(1)
"""
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        res = sys.maxsize
        
        index_1 = -1
        index_2 = -1
        
        
        for i in range(len(words)):
            
            if words[i] == word1:
                index_1 = i
            
            if words[i] == word2:
                index_2 = i
                
                
            if index_1 >= 0 and index_2 >= 0:
                res = min(res, abs(index_1 - index_2))
                
        return res