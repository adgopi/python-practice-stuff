class Solution:
    # def __init__(self):
    #     self.store = {0:0, 1:1}
 
    def fibo(self, n: int) -> int:
        # if n in self.store:
        #     return self.store[n]
        if n == 0:
            return n
        else:
            # self.store[n-1] = self.fibo(n-1)
            # self.store[n-2] = self.fibo(n-2)
            # return self.store[n-2] + self.store[n-1]
            
            # self.store[n] = self.fibo(n-1) + self.fibo(n-2)
            # return self.store[n]
            current = 1
            prev = 0
            for i in range(2,n+1):
                temp = current
                current = current + prev
                prev = temp
            return current

S = Solution()
print(S.fibo(50))

# fibo(2) = fibo(1) + fibo(0)
# fibo(3) = fibo(2) + fibo(1)
# fibo(4) = fibo(3) + fibo(2) 
# current = prev + prevprev

# 4
# 3, 2
# 2,1  1,0
# 1,0 [] [] [] [] 
# 1

# 3
# 2, 1
# 1,0 | []


# 2^N N --> N N --> N 1