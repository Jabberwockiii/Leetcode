class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        naive approach is to have a double for loop for every element if it is adds up
        to the same 
        """
        #to achive a O(n) time complexity, we can use a hash table
        #dict to store the index of the number
        #enumerate the list
        hashtable = {}
        for i, num in enumerate(nums):
            #find the complement
            complement = target - num
            if complement in hashtable:
                return [hashtable[complement], i]
            else:
                hashtable[num] = i

                