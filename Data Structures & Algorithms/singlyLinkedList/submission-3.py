class Node:
    def __init__(self, value=None, next= None):
        self.value= value
        self.next= next


class LinkedList:
    
    def __init__(self):
        self.head= None
        self.tail= None
    
    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        i=0;
        cur= self.head
        while(i<index and cur.next is not None):
            cur= cur.next
            i += 1
        if i==index:
           return cur.value
        return -1

    def insertHead(self, val: int) -> None:
        node= Node(value=val)
        node.next= self.head
        self.head= node
        if self.tail is None:
            self.tail=node

    def insertTail(self, val: int) -> None:
        node= Node(value=val)
        if self.tail is not None:
           self.tail.next= node
        if self.head is None:
            self.head= node
        self.tail= node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        i=0;
        cur= self.head
        prev= None;
        while(i<index and cur.next is not None):
            prev= cur
            cur= cur.next
            i += 1
        if i<index:
           return False
        if self.tail==cur:
            self.tail=prev
        if prev:
            prev.next= cur.next
        if index==0:
           self.head= cur.next
        return True

    def getValues(self) -> List[int]:
        val_list=[]
        cur= self.head
        if self.head is None:
           return val_list
        val_list.append(cur.value)
        while(cur.next is not None):
            cur= cur.next
            val_list.append(cur.value)
        return val_list

        
