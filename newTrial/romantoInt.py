class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman = {'I':1, 'IV' : 4, 'V':5, 'IX': 9, 'X':10, 'XL':40, 'L':50, 'XC':90,'C':100, 
                 'CD': 400, 'D':500, 'CM':900, 'M':1000}
        i = 0
        j = 1
        num = 0
        while j < len(s) and i < j:
            oneSeg = s[i:j]
            twoSeg = s[i:j+1]
            if twoSeg in Roman or oneSeg in Roman:
                i = j
                j += 1
                num += Roman[oneSeg] if oneSeg in Roman else Roman[twoSeg]
        return num
            