class Solution:

    def climbStairs(self, n: int) -> int:
        prev, current= 1,2

        if n==1:
            return 1
        if n==2:
            return 2

        for i in range(3,n):
            next_val= prev+current
            prev= current
            current= next_val
        
        return current+prev
        