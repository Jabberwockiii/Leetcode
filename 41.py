class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        #answer range[1,n+1]
        #exclude negative number and number bigger than n+1
        for i in range(n):
            if nums[i] < 0 or nums[i] > n:
                nums[i] = 0
        nums.sort()
        for i in range(n):
            if(nums[i] == 0):
                continue
            if(nums[i] == nums[i-1] + 1):
                continue
            else:
                return nums[i-1] + 1
        return nums[n-1] + 1 
s = Solution()
print(s.firstMissingPositive([2,2]))