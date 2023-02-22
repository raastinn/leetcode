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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result;
        ListNode cur;
        int newVal = 0;
        int remainder = 0;
        int incrementBy = 0;
        newVal = l1.val + l2.val;
        if (newVal >= 10) {
            newVal = newVal - 10;
            incrementBy = 1;
        }
        cur = result = new ListNode(newVal);
        l1 = l1.next;
        l2 = l2.next;
        while (l1 != null && l2 != null) {
            newVal = incrementBy + l1.val + l2.val;
            if (newVal >= 10) {
                newVal = newVal - 10;
                incrementBy = 1;
            } else {
                incrementBy = 0;
            }
            cur.next = new ListNode(newVal);
            System.out.println(""+newVal);
            l1 = l1.next;
            l2 = l2.next;
            cur = cur.next;
        }
        // empty the l1 nodes if l1 size > l2 size
        while (l1 != null) {
            newVal = incrementBy + l1.val;
            if (newVal >= 10) {
                newVal = newVal - 10;
                incrementBy = 1;
            } else {
                incrementBy = 0;
            }
            System.out.println(""+newVal);
            cur.next = new ListNode(newVal);
            l1 = l1.next;
            cur = cur.next;
        }
        // empty the l2 nodes if l2 size > l1 size
        while (l2 != null) {
            newVal = incrementBy + l2.val;
            if (newVal >= 10) {
                newVal = newVal - 10;
                incrementBy = 1;
            } else {
                incrementBy = 0;
            }
            cur.next = new ListNode(newVal);
            l2 = l2.next;
            cur = cur.next;
        }
        // See if there is a remainder after all nodes added
        if (incrementBy == 1) {
            cur.next = new ListNode(1);
        }
        return result;
    }
}
