# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        #if head does not exist (linked list is 0) then return None
        newHead = head
        #initialize out a new head 
        if head.next: # if theres a next node move pointer to next node and point backwards then do the recursive function then iterate until there is no next node. 
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead

        




        