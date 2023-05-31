#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode()
        new2 = new
        tmp = 0
        while l1 or l2:
            v = tmp
            if l1:
                v+=l1.val
                l1 = l1.next
            if l2:
                v+=l2.val
                l2 = l2.next
            
            tmp = v//10
            v = v%10
            
            new2.next = ListNode(v)
            new2 = new2.next
        
        if tmp:
            new2.next = ListNode(tmp)
        
        return new.next
# @lc code=end

