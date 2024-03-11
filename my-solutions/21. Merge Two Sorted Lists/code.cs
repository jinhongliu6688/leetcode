/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        ListNode s = new ListNode();
        ListNode p = s;

        ListNode h1 = list1;
        ListNode h2 = list2;

        while (h1 != null && h2 != null) 
        {
            if (h1.val < h2.val)
            {
                p.next = h1;
                h1 = h1.next;
            }
            else
            {
                p.next = h2;
                h2 = h2.next;
            }
            p = p.next;
        }

        if (h1 != null) p.next = h1;
        else if (h2 != null) p.next = h2;

        return s.next;
    }
}
