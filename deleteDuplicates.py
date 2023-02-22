# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            cur = head
            while (cur.next):
                if cur.val == cur.next.val:
                    if cur.next.next:
                        cur.next = cur.next.next
                    else:
                        cur.next = None
                    continue
                cur = cur.next
        return head
        
