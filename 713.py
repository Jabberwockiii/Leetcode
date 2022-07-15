class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        l = 0
        res = 0
        product = 1
        
        for r in range(len(nums)):
            product *= nums[r]
            
            if product >= k:
                while product >= k and l <= r:
                    product /= nums[l]
                    l += 1
            
            res += r - l + 1
        return res
s = Solution()
print(s.numSubarrayProductLessThanK([10,5,2,6], 100))