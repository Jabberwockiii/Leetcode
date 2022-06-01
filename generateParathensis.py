class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.helper(n, 0, 0, '', res)
        return res
    def helper(self, n, left, right, path, res):
        if left == n and right == n:
            res.append(path)
            return
        if left < n:
            self.helper(n, left + 1, right, path + '(', res)
        if right < left:
            self.helper(n, left, right + 1, path + ')', res)