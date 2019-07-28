import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for i in range(len(nums)):
            heapq.heappush(q,nums[i])
        j = len(nums)-k+1
        while j:
            num = heapq.heappop(q)
            j -=1
        return num

#nums[:k]做成heap
#循环比较剩下的数值如果大于q[0]
#pop q[0] push[那个数值]
#最后pop q[0]