import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if not self.maxheap :# 因为大堆比小堆多 所以判断大堆是否为空就ok
            heapq.heappush(self.maxheap,num)
        elif num > self.maxheap[0]:
            heapq.heappush(self.maxheap, num)
        else:
            heapq.heappush(self.minheap, -num)

        while len(self.maxheap) - len(self.minheap) < 0 :
            n = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -n)

        while len(self.maxheap) - len(self.minheap) >1 :
            n = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -n)


    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap) :
            result = (self.maxheap[0]-self.minheap[0])/2
        else:
            result = self.maxheap[0]

        return  result


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.findMedian()


