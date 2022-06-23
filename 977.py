class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            s = nums[0] * nums[0]
            return [s]
        p1 = 0
        p2 = len(nums) - 1
        result = []
        while(p1 < p2):
            s1 = nums[p1] * nums[p1]
            s2 = nums[p2] * nums[p2]
            if (s1 < s2):
                result.append(s2)
                p2 -= 1
            else:
                result.append(s1)
                p1 += 1
        result.append(nums[p1]*nums[p1])
        return result[::-1]
                
            
            
        