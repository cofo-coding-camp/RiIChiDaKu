# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        p = head
        count = 1
        while p.next:
            p = p.next
            count += 1
        p.next = head
        n = count - k % count
        q = p

        for _ in range(n):
            q = q.next
        p = q.next
        q.next = None

        return p

