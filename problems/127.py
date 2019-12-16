"""
127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

Solution:
We perform a BFS on the begin word to the end word. We can resemble the edges as a change for each letter. For example: the word hit:
hit --> *it
    --> h*t ==> hot --> *ot --> ==> dot
   					-->	h*t
   					-->	ho*
    --> hi*
and from there we can branch off to the next word.

Runtime: O(N)
Space: O(N)
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordListSet = set(wordList)
        queue = []
        res = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        if endWord not in wordListSet:
            return 0
        
        
        
        queue.append({"word": beginWord, "level": 1})
        
        
        while len(queue) > 0:
            
            # Grab current word from queue
            item = queue.pop(0)
            current_word = list(item["word"])
            level = item["level"]
            
            if ''.join(current_word) in wordListSet:
                wordListSet.remove(''.join(current_word))
            
            # Loop through each position of the word
            for i in range(len(current_word)):
                
                # Keep track of the original letter
                original_letter = current_word[i]
                
                # Replace the position with every character in the alphabet
                for letter in alphabet:
                    current_word[i] = letter
                    
                    new_word = ''.join(current_word)
                    
                    # If the new word is in the set we append to queue
                    if new_word == endWord:
                        return level + 1
                    if new_word in wordListSet:
                        wordListSet.remove(new_word)
                        queue.append({"word": new_word, "level": level + 1})
                        
                        
                        
                
                current_word[i] = original_letter
        return res