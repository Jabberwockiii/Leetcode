class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if (len(nums) < 3):
            return []
        result = []
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            #store the content 
            while (j < k):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
        return list(set(result))
        
            
                
                
                
        