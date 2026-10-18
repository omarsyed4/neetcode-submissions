class MyHashSet:

    def __init__(self):
        self.fullSet = []
        

    def add(self, key: int) -> None:
        if key in self.fullSet:
            return
        else:
            self.fullSet.append(key)
        

    def remove(self, key: int) -> None:
        if key not in self.fullSet:
            return
        else:
            for i, num in enumerate(self.fullSet):
                if num == key:
                    self.fullSet[i], self.fullSet[-1] = self.fullSet[-1], self.fullSet[i]
        self.fullSet = self.fullSet[:-1]

    def contains(self, key: int) -> bool:
        for i, num in enumerate(self.fullSet):
            if num == key:
                return True
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)