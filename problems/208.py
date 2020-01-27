"""
208. Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.


"""

class Node(object):
    def __init__(self, alphabet, isFinal):
        
        self.alphabet = alphabet
        self.isFinal = isFinal
class Trie(object):

    def __init__(self):
        
        self.root = {}
        
    def insert(self, word):
        node = self.root
        
        for i in range(len(word)):
            letter = word[i]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node["isWord"] = True
        
    def searchPrefix(self, word):
        node = self.root
        for i in range(len(word)):
            letter = word[i]
            if letter not in node:
                return None
            node = node[letter]
        return node
    def search(self, word):
        
        node = self.searchPrefix(word)
        return ((node is not None) and ("isWord" in node))
        

    def startsWith(self, prefix):
        
        node = self.searchPrefix(prefix)
        return (node is not None)


