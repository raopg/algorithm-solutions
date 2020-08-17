## Implementation of the Trie data structure.

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end = True

class Trie:
    def __init__(self):
        self.root = TrieNode(None)
    
    def insert(self, word):
        parent = self.root
        for i, char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = TrieNode(char)
            parent = parent.children[char]
            if i == len(word) - 1:
                parent.end = True

    def search(self, word):
        parent = self.root
        for char in word:
            if char not in parent.children:
                return False
            parent = parent.children[char]

        return parent.ends
    
    def startsWith(self, prefix):
        ret = []
        parent = self.root
        for char in prefix:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return True
    
    