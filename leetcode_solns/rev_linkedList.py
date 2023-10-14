"""

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head 
        else:
            l1 = ListNode(-1)
            l2 = l1  

            index = 1 
            current = head
            for i in range(1,left):
                current = current.next 

            revList = ListNode(-1)
            rever = revList

            current2 = current 

            

            for j in range((right-left)+1):
                rever.next = ListNode(current2.val)
                current2 = current2.next 
                rever = rever.next 

            revList = revList.next

            

            prev = None 
            curr = revList 
            while curr:
                temp = curr.next 
                curr.next = prev 
                prev = curr 
                curr = temp 

            burr = head
            for k in range(right):
                burr = burr.next 

            
            newprev = prev 
            while newprev.next:
                newprev = newprev.next

            newprev.next = burr

            for i in range(left-1):
                l2.next = ListNode(head.val)
                head = head.next
                l2 = l2.next

            l2.next = prev 

            return l1.next