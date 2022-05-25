class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        #two pointers to check if it is a palindrome
        if len(str_x) == 1:
            return True
        elif len(str_x) == 2:
            if str_x[0] == str_x[1]:
                return True
        else:
            return str_x[0] == str_x[-1] and self.isPalindrome(int(str_x[1:-1]))
