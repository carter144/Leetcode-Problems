"""
269. Alien Dictionary

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.

Solution:
1. Create a graph from the input
2. Check if the graph has a cycle, if it does then the order is invald
3. Return the topological sort of the graph
"""

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    
    def hasCycle(self, current, whiteSet, greySet, blackSet):

        if current in whiteSet:
            whiteSet.remove(current)
        if current in greySet:
            return True
        if current in blackSet:
            return False
        greySet.add(current)
        for neighbor in current.neighbors:
            if (self.hasCycle(neighbor, whiteSet, greySet, blackSet)):
                return True
        
        greySet.remove(current)
        blackSet.add(current)
        return False
    
        
        
    def topSort(self, current, visited, stack):
        if current in visited:
            return
        visited.add(current)
        if len(current.neighbors) == 0:
            stack.append(current)
            return
        
        for neighbor in current.neighbors:
            self.topSort(neighbor, visited, stack)
        stack.append(current)
        return
        
    
    
    def alienOrder(self, words: List[str]) -> str:
        edges = []
        edge_set = set()
        letters = set()
        if len(words) == 1:
            return words[0]
        for i in range(len(words) - 1):
            
            word1 = words[i]
            word2 = words[i + 1]
            
            letter1 = word1[0]
            letter2 = word2[0]
            
            for letter in word1:
                letters.add(letter)
                
            for letter in word2:
                letters.add(letter)
            i = 0
            while i < len(word1) and i < len(word2):
                char1 = word1[i]
                char2 = word2[i]
                letters.add(char1)
                letters.add(char2)
                if char1 != char2:
                    combination = char1 + char2
                    if combination not in edge_set:
                        edge_set.add(combination)
                    break
                        
                i += 1
            
        
        nodes = {}
        
        
        for letter in letters:
            
            nodes[letter] = Node(letter, [])
        
        for edge in edge_set:
            first = edge[0]
            second = edge[1]
            nodes[first].neighbors.append(nodes[second])
            print(edge)
        
        whiteSet = set()
        greySet = set()
        blackSet = set()
        
        for node in nodes:
            whiteSet.add(nodes[node])
        for node in nodes:
            if self.hasCycle(nodes[node], whiteSet, greySet, blackSet):
                return ""
        visited = set()
        stack = []
        for node in nodes:
            
            self.topSort(nodes[node], visited, stack)
            
        res = []
        for item in stack:
            res.append(item.val)
        return ''.join(res[::-1])
        