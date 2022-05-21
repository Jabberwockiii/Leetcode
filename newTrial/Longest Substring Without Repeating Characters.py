class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #pass in a string and return the length of the longest substring without repeating characters
        #using two pointers 
        #using a dictionary to keep track of the characters in the substring
        left_pointer = 0
        right_pointer = 0
        current_unrepeated_substring = []
        longest_substring = 0
        while right_pointer < len(s):
            if s[right_pointer] not in current_unrepeated_substring:
                current_unrepeated_substring.append(s[right_pointer])
                right_pointer += 1
            else:
                #if the character is already in the substring, then we need to remove the leftmost character
                #and move the left pointer to the right
                current_unrepeated_substring.remove(s[left_pointer])
                left_pointer += 1
            longest_substring = max(longest_substring, len(current_unrepeated_substring))
        return longest_substring