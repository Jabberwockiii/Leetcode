class Solution:
    def trap(self, height):
        leftMax = 0
        rightMax = 0
        result = 0
        for i, j in enumerate(height):
            for k in range(i):   
                leftMax = max(leftMax, height[k])
            for k in range(i, len(height)):
                rightMax = max(rightMax, height[k])
            result += min(leftMax, rightMax) - j
        return result

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))