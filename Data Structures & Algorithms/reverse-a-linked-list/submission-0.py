# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            #1 save nxt node
            nxt = curr.next
            #2 point pointer backwards
            curr.next = prev
            #3 move prev forward
            prev = curr
            #4 move curr forward
            curr = nxt

        return prev 