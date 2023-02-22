# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        given1 = []
        given2 = []
        cur = l1
        while cur:
            given1.append(l1.val)
            cur = l1.next
        print(given1)
