class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if (len(nums) < 3):
            return []
        result = []
        nums.sort()
        smallest = float('inf')
        content = 0
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            #store the content 
            while (j < k):
                difference = abs(target - (nums[i] + nums[j] + nums[k]))
                if difference < smallest:
                    smallest = difference
                    content = nums[i] + nums[j] + nums[k]
                    k -= 1
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
        return content