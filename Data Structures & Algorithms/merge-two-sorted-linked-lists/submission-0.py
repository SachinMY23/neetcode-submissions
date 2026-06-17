# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is not None and list2 is None:
           return list1
        elif list2 is not None and list1 is None:
            return list2
        elif list1 is None and list2 is None:
            return None

        cur1= list1
        cur2= list2
        head= None
        tail= None
        sorted_list=None
        while(cur1 is not None and cur2 is not None):
            if cur1.val<=cur2.val:
                item= ListNode(val= cur1.val)
                if head is None:
                    head= item
                if tail is not None:
                    tail.next= item
                tail= item
                cur1= cur1.next
                
            elif cur1.val>cur2.val:
                item= ListNode(val= cur2.val)
                if head is None:
                    head= item
                if tail is not None:
                    tail.next= item
                tail= item
                cur2= cur2.next


        while(cur1 is not None):
            item= ListNode(val= cur1.val)
            if head is None:
                head= item
            if tail is not None:
                tail.next= item
            tail= item
            cur1= cur1.next

        while(cur2 is not None):
            item= ListNode(val= cur2.val)
            if head is None:
                head= item
            if tail is not None:
                tail.next= item
            tail= item
            cur2= cur2.next

        return head



