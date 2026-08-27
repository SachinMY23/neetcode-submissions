class Pages:
    def __init__(self, url=None):
        self.url= url
        self.nxt= None
        self.prev= None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.size=1
        self.head= Pages(url=homepage)
        self.tail= Pages(url= homepage)
        self.tail.prev= self.head

    def visit(self, url: str) -> None:
        visit_page= Pages(url= url)
        if self.tail.url is None:
           self.tail.url= url
        elif self.tail.url is not None:
            visit_page.prev= self.tail
            self.tail.nxt= visit_page
            self.tail= visit_page

    def back(self, steps: int) -> str:
        inc_steps=0
        inc_page= self.tail
        while(inc_steps<steps and inc_page.prev is not None):
            inc_page= inc_page.prev
            inc_steps += 1
        self.tail= inc_page
        print(f"{self.tail.nxt}")
        return self.tail.url

    def forward(self, steps: int) -> str:
        print(f"Forwarding")
        print(f"Tail:{self.tail.nxt}")
        inc_steps=0
        inc_page= self.tail
        while(inc_steps<steps and (inc_page.nxt is not None)):
            print(f"Forwarding: {inc_page}")
            inc_page= inc_page.nxt
            inc_steps += 1
        self.tail= inc_page
        return self.tail.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)