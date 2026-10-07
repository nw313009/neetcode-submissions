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
            nxt = curr.next
            #point pointer backwards
            curr.next = prev
            #move prev forward to curr
            prev = curr
            #move curr
            curr = nxt

        return prev
        




        