class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #use dp to store the state that whether it is a palindrome 
        longestPalindrome = ''
        #use i, j to construct a 2 dimensional dp, i is the row index and j is the column index
        dp = [[0]*len(s) for _ in range(len(s))]
        #fill the dp with diagonal as single character is always true 
        for i in range(len(s)):
            dp[i][i] = 1
            longestPalindrome = s[i]
        # change the indexing to the right bottom of the dp matrix so that we can determine if the substring is a palindrome
        for i in range(len(dp) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                # if the substring is a palindrome, then the substring is the longest palindrome
                if s[i] == s[j]:
                    # 'bb' case
                    if j - i == 1 or dp[i + 1][j - 1] == 1:
                        dp[i][j] = 1
                    if len(s[i:j+1]) > len(longestPalindrome):
                        longestPalindrome = s[i:j+1]
        return longestPalindrome
                    