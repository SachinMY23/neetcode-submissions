class ListNode:

    def __init__(self):
        self.nxt= None
        self.prev= None
        self.val= None;

class MyLinkedList:
    
    def __init__(self):
        self.head= ListNode()
        self.tail= ListNode()
        self.count= 0

    def get(self, index: int) -> int:
        idx= 0
        item= self.head
        while idx<index and item:
            idx += 1
            item= item.nxt
        return item.val if (item and item.val>=0 and idx==index) else -1

    def getItemAtIndex(self, index: int) -> int:
        if self.count==0 or self.count==index:
            return -1
        elif self.count-1==index:
            return self.tail
        item= self.head
        idx=0
        while index>idx:
            idx += 1
            print(item.val)
            item= item.nxt
        return item

    def addAtHead(self, val: int) -> None:
        item= ListNode()
        item.val= val
        if self.head.val is not None:
           self.head.prev= item
           item.nxt= self.head
           if self.tail.val is None:
              self.tail= self.head
        self.head= item
        self.count+=1

    def addAtTail(self, val: int) -> None:
        item= ListNode()
        item.val= val
        if self.tail.val is not None:
            item.prev= self.tail
            self.tail.nxt= item
        elif self.tail.val is None and self.head.val is not None:
            item.prev=self.head
            self.head.nxt= item
        self.tail= item
        self.count+=1
    
    def addAtIndex(self, index: int, val: int) -> None:
        print(f"Adding at index {index} value {val}")
        if self.count==index:
           self.addAtTail(val)
           return
        item= self.getItemAtIndex(index)
        prev_item= item.prev
        insert_item= ListNode()
        insert_item.val= val
        item.prev= insert_item
        insert_item.nxt= item
        insert_item.prev= prev_item
        prev_item.nxt= insert_item
        self.count += 1
        
    def deleteAtIndex(self, index: int) -> None:
        print(f"Deleting at index")
        if index>=self.count:
            return
        if self.count==1:
           self.head= ListNode()
           self.tail= ListNode()
        elif self.count==2:
            if index==0:
                self.head= self.tail
                self.head.prev= None
                self.tail= ListNode()
            elif index==1:
                self.head.nxt= None
                self.tail= ListNode()
        elif self.count-1==index:
            item= self.tail.prev
            item.nxt= None
            self.tail= item
        else:
            item= self.getItemAtIndex(index)
            item.prev.nxt= item.nxt
            item.nxt.prev= item.prev
        self.count -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)