import math
class Solution:
    def numSquares(self, n: int) -> int:
        def helper(n):
            if n in memo:
                return memo[n]
            if n < 0:
                return 0
            n1 = math.floor(math.sqrt(n))
            m = n1
            for i in range(1, n1 + 1):
                s = i * i
                m = min(1+helper(n-s), m) + 1
            memo[n] = m
            return m
        memo = {}
        return helper(n)
s = Solution()
print(s.numSquares(12))