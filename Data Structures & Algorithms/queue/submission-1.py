class Node():

    def __init__(self, val=None):
        self.val= val
        self.prev= None
        self.nxt = None

class Deque:
    
    def __init__(self):
        self.head= None
        self.tail= None

    def isEmpty(self) -> bool:
        return True if self.head is None else False

    def append(self, value: int) -> None:
        print(f"Appending{value}")
        item= Node(value)
        if self.head is None:
            self.head= item
            if self.tail is None:
                self.tail= self.head
        elif self.tail==self.head:
            self.tail= item
            self.tail.prev= self.head
            self.head.nxt= self.tail
        else:
            item.prev= self.tail
            self.tail.nxt= item
            self.tail= item
        print(f"tail: {self.tail.val}")

    def appendleft(self, value: int) -> None:
        item= Node(value)
        if self.head is None:
            self.head= item
            if self.tail is None:
                self.tail= self.head
        else: 
            item.nxt= self.head
            self.head.prev= item
            if self.tail==self.head:
                self.tail= self.head
            self.head=item

    def pop(self) -> int:
        if self.tail is not None:
            item= self.tail
            if item==self.head:
                self.head= self.tail= None
            else:
                self.tail= item.prev
            return item.val
        return -1

    def popleft(self) -> int:
        if self.head is not None:
            item= self.head
            if self.head==self.tail:
               self.head= self.tail= None
            elif item.nxt:
                self.head= item.nxt
            return item.val
        return -1
        
