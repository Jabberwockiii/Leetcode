#
# def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         len1 = len(nums1)
#         len2 = len(nums2)
#         # when total length is odd, the median is the middle
#         if (len1 + len2) % 2 != 0:
#             return self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2)
#         else:
#         # when total length is even, the median is the average of the middle 2
#             middle1 = self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2)
#             middle2 = self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2-1)
#             return (middle1 + middle2) / 2

#     def get_kth(self, nums1, nums2, start1, end1, start2, end2, k):
#         if start1 > end1:
#             return nums2[k-start1]
#         if start2 > end2:
#             return nums1[k-start2]
        
#         middle1 = (start1 + end1) // 2
#         middle2 = (start2 + end2) // 2
#         middle1_value = nums1[middle1]
#         middle2_value = nums2[middle2]
        
#         # if sum of two median's indicies is smaller than k
#         if (middle1 + middle2) < k:
#             # if nums1 median value bigger than nums2, then nums2's first half will always be positioned before nums1's median, so k would never be in num2's first half
#             if middle1_value > middle2_value:
#                 return self.get_kth(nums1, nums2, start1, end1, middle2+1, end2, k)
#             else:
#                 return self.get_kth(nums1, nums2, middle1+1, end1, start2, end2, k)
#         # if sum of two median's indicies is bigger than k
#         else:
#             # if nums1 median value bigger than nums2, then nums2's first half would be merged before nums1's first half, thus k always come before nums1's median, then nums1's second half would never include k
#             if middle1_value > middle2_value:
#                 return self.get_kth(nums1, nums2, start1, middle1-1, start2, end2, k)
#             else:
#                 return self.get_kth(nums1, nums2, start1, end1, start2, middle2-1, k)
            
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
    #find the kth smallest of the merged sorted array of a and b
    # k is the index value of the kth smallest element
        single_median = (len(nums1) + len(nums2)) // 2
        double_median = (len(nums1) + len(nums2)) // 2 - 1
        if len(nums1) + len(nums2) == 0:
            return None
        elif (len(nums1) + len(nums2)) % 2 == 1:
            return self.find_kth_smallest(nums1, nums2, 0, len(nums1) - 1, 0, len(nums2) - 1, single_median)
        elif (len(nums1) + len(nums2)) % 2 == 0:
            val1 = self.find_kth_smallest(nums1, nums2, 0, len(nums1) - 1, 0, len(nums2) - 1, single_median)
            val2 = self.find_kth_smallest(nums1, nums2, 0, len(nums1) - 1, 0, len(nums2) - 1, double_median)
            return val1 + val2 / 2
    def find_kth_smallest(self, a, b, a_start, a_end, b_start, b_end, k):
        #base case 
        if a_start > a_end:
            return b[k - a_start]
        elif b_start > b_end:
            return a[k - b_start]
        else:
            #case that both a and b are normal with length m and n
            middle1 = (a_start + a_end) // 2
            middle2 = (b_start + b_end) // 2
            middle1_value = a[middle1]
            middle2_value = b[middle2]

            #determine where is k
            if middle1 + middle2 < k:
                if middle1_value > middle2_value:
                    #since middle1 > middle2
                    #exclude some parts 
                    return self.find_kth_smallest(a, b, a_start, a_end, middle2 + 1, b_end, k)
                else:
                    return self.find_kth_smallest(a, b, middle1 + 1, a_end, b_start, b_end, k)
            else:
                if middle1_value > middle2_value:
                    return self.find_kth_smallest(a, b, a_start, middle1 - 1, b_start, b_end, k)
                else:
                    return self.find_kth_smallest(a, b, a_start, a_end, b_start, middle2 - 1, k)
            
            
            
        
        
        