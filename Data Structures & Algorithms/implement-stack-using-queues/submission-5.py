from collections import deque

class MyStack:

    def __init__(self):
        self.queue1= deque()
        self.queue2= deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)
        print(self.queue1.maxlen)

    def pop(self) -> int:
        elem= self.queue1.pop()
        return elem

    def top(self) -> int:
        return self.queue1[-1]
        
    def empty(self) -> bool:
        try:
            if self.queue1[-1] is not None:
                return False
        except Exception as e:
            return True
       


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()