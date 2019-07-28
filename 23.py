# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = []#新建一个堆
        head = n = ListNode(0)#头节点
        step = 0
        for list in lists:
            while list:
                #step 和 id() 意义一样 用于区分一样的数值 防止比较到list链表这一步 因为比较不了
                # 存到heap里的是一个set
                heapq.heappush(q, (list.val, step, list))
                list = list.next
                step += 1
        while q:
            #加到新链表里的是链表元素
            n.next = heapq.heappop(q)[-1]
            n = n.next
        return head.next

