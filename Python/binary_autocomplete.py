## Problem: Given a sequence of binary commands entered into a console, return the last
## command which shares the longest common prefix with the current command. If there is no such previous command
## then the last command is shown
## For the first command, the corresponding answer will be 0.
## Return a list of prev commands for a list of given commands.
## Example: ['000', '1110', '01', '001', '110', '11']

## Solution: Use a prefix tree.
## The modification is, we need a way to identify which command the matching prefix belongs to
## We can use a value within the TrieNode that contains a last_command field, corresponding to the index
## of the last command that the TrieNode belongs to.

class TrieNode:
    def __init__(self, val = None, last_command = None):
        self.val = val
        self.last_command = last_command
        self.children = {}
        self.ends_here = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, index):
        parent = self.root

        for i, char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = TrieNode(char)
            parent = parent.children[char]
            parent.last_command = index
            if i == len(word) - 1:
                parent.ends_here = True
    
    def last_command_prefix(self, word):
        last_command_index = None
        parent = self.root
        for char in word:
            last_command_index = parent.last_command
            if char not in parent.children:
                break
            parent = parent.children[char]
        
        return last_command_index

def binary_autocomplete(commands):
    if not commands:
        return []
    if len(commands) == 1:
        return [0]
    
    t = Trie()
    t.insert(commands[0], 1)
    ret = [0]

    for i in range(1, len(commands)):
        last_index = t.last_command_prefix(commands[i])

        if not last_index:
            ret.append(i)
        else:
            ret.append(last_index)

        t.insert(commands[i], i+1)
    
    return ret


if __name__ == "__main__":
    commands = ['000', '1110', '01', '001', '110', '11']

    print(binary_autocomplete(commands))
    
