class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        
        
    def addWord(self, word: str) -> None:
        ptr = self.root

        for i, c in enumerate(word):
            if c not in ptr.children:
                ptr.children[c] = TrieNode()
            ptr = ptr.children[c]
        
        ptr.end = True
        
        return

    def search(self, word: str) -> bool:

        def dfs(ptr, word):
            if not word:
                return ptr.end

            c = word[0]

            if c == ".":
                for child in ptr.children.values():
                    if dfs(child, word[1:]):
                        return True
                return False

            if c not in ptr.children:
                return False

            return dfs(ptr.children[c], word[1:])

        return dfs(self.root, word)


        
