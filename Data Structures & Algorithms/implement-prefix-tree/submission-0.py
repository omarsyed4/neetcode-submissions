class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        ptr = self.root
        for i, c in enumerate(word):
            if c in ptr.children:
                ptr = ptr.children[c]
                if (i == (len(word) - 1)):
                    ptr.end = True
                continue
            else:
                ptr.children[c] = TrieNode()
                ptr = ptr.children[c]
                if (i == (len(word) - 1)):
                    ptr.end = True
                continue


    def search(self, word: str) -> bool:
        ptr = self.root
        for i, c in enumerate(word):
            if c in ptr.children:
                ptr = ptr.children[c]
                if (i == (len(word) - 1)):
                    if ptr.end == True:
                        return True
                    else:
                        return False
                continue
            else:
                return False
        return False

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for i, c in enumerate(prefix):
            if c in ptr.children:
                ptr = ptr.children[c]
                if (i == (len(prefix) - 1)):
                    return True
                continue
            else:
                return False

        # Iterate through the string for all letters. 
        # Make a pointer to the root. 
        # Look through the children of the root for the first letter. 
        # Once you get a match, move the pointer and the traversal of the string. 
        # When you can't find a match, return false. 
        # When you found all letters, return true 