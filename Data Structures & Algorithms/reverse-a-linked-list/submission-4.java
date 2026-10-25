/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        //base case
        if (head == null || head.next== null) {
            return head;
        }

        //reverse rest of list
        ListNode newHead = reverseList(head.next);

        //rearrange the pointers
        head.next.next = head;

        //break the original forward link to avoid cycles
        head.next = null;

        //Return the new head of the reversed list
        return newHead;
    }
}
