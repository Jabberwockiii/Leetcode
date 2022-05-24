class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #build an array of strings to store the result
        if numRows == 1 or numRows >= len(s):
            return s
        matrix = [''] * numRows
        direction = 1
        row = 0
        for i in range(len(s)):
            matrix[row] += s[i]
            if row == 0:
                direction = 1
            if row == numRows - 1:
                direction = -1
            row += direction
        return ''.join(matrix)