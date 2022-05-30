# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = list1
        while(list1.next != None or list2.next != None):
            if(list1.next == None):
                list1.next = list2
                break
            elif(list2.next == None):
                list2.next = list1
                break
            elif(list1.val < list2.val):
                list1.next = list2
                list2 = list2.next
            elif(list1.val >= list2.val):
                prev = list1
                list2.next = list1
                list1 = prev
        return head 
        
                
            
        