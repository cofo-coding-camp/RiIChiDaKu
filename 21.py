# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        n = ListNode(0)
        p = n
        while l1 and l2:
            if l1.val < l2.val:
                p.next = ListNode(l1.val)
                l1 = l1.next
                p = p.next
            else:
                p.next = ListNode(l2.val)
                l2 = l2.next
                p = p.next
        p.next = l1 if l1 else l2

        return n.next


