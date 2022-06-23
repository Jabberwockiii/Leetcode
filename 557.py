class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        k = s.split()
        for i in k:
            l = 0
            r = len(i) - 1
            while(l < r):
                i[l], i[r] = i[r], i[l]
                l += 1
                r -= 1
        k = ' '.join(k)
        return k
s = Solution()
print(s.reverseWords("the sky is blue"))