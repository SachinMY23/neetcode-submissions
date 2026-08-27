class MyStack:

    def __init__(self):
        self.c_stack= []
        self.current_elem= -1

    def push(self, x: int) -> None:
        self.c_stack.insert(self.current_elem+1, x)
        self.current_elem += 1

    def pop(self) -> int:
        if self.current_elem>=0:
            elem= self.c_stack[self.current_elem]
            self.current_elem -= 1
        return elem


    def top(self) -> int:
        return self.c_stack[self.current_elem]
        
    def empty(self) -> bool:
        return not self.current_elem>=0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()