class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        l = len(self.arr)
        if l % 2 == 1:
            i = l // 2
            return self.arr[i]
        else:
            i = l // 2
            return (self.arr[i] + self.arr[i-1]) / 2
        