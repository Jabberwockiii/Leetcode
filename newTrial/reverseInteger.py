class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #store the number in a doublely linked list and reverse the list
        result = 0
        negative = 0
        if x < 0:
            x = -x
            negative = 1
        if x >= 2**31-1or x <= -2**31:
            return 0
        while(x != 0):
            lastDigit = x % 10
            x = x // 10
            result = result * 10 + lastDigit
        if negative == 1:
            result = -result
        if result >= 2**31 -1 or result <= -2**31:
            return 0
        else:
            return result             
        