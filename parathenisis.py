class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {"{": "}", "[": "]", "(": ")"}
        stack = []
        for i in s:
            if i in pairs:
                stack.append(i)
            elif not stack or pairs[stack.pop()] != i:
                return False
        return not stack
        

        