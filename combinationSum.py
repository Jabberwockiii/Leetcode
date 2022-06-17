class Solution(object):
    def combinationSum2(self, candidates, target):
        ret = []
        self.dfs(sorted(candidates), target, 0, [], ret)
        return ret
    
    def dfs(self, nums, target, idx, path, ret):
        if target <= 0:
            if target == 0:
                ret.append(path)
            return 
        for i in range(idx, len(nums)):
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], ret)
s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))