
class Solution:
    def numSquares(self, n: int) -> int:
        def helper(n):
            if n in memo:
                return memo[n]
            if n < 0:
                return 0
            n1 = math.floor(math.sqrt(n))
            m = 100
            for i in range(1, n1 + 1):
                s = i * i
                m = min(1+helper(n-s), m)
            memo[n] = m
            return m
        memo = {}
        m = float('inf')
        return helper(n)
s = Solution()
print(s.numSquares(12))
