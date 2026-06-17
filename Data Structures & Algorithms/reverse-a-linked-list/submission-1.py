# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val= []
        if head is None:
            return None
        cur= head
        prev_node= None
        while(cur.next is not None):
            temp_cur= cur
            cur= cur.next
            temp_cur.next= prev_node
            prev_node= temp_cur
        
        cur.next= prev_node
        head=cur
        while(cur.next is not None):
             val.append(cur.val)
             cur=cur.next
        return head


        