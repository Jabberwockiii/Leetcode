# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         #use recursion to find the max area
#         return self.helper(height, 0, len(height)-1)
#     def helper(self, height, l, r):
#         if l == r:
#             return 0
#         elif l < r:
#             current_area = (r-l)*min(height[l], height[r])
#         max_area = max(current_area, max(self.helper(height, l+1, r), self.helper(height, l, r-1)))
#         return max_area
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #two pointers 
        l = 0
        r = len(height)-1
        max_area = 0
        # why using the two pointers?
        # maintaining the maximum width of the container
        
        while l < r:
            max_area = max(max_area, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
            