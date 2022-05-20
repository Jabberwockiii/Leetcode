class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        naive approach is to have a double for loop for every element if it is adds up
        to the same 
        """
        #enumerate the list 
        #time complexity of enumeraiton is O(n)
        for i, num in enumerate(nums):
            #find the complement 
            complement = target - num
            #find the complement in the list
            #time complexity is O(n)
            #slicing in python is O(1), and the 
            if complement in nums[i+1:]:
                #return the index of the complement
                return [i, nums.index(complement, i+1)]
        #total time complexity is O(n^2)
        
        