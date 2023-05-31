#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        max_len = 1
        p1,p2=0,1
        while p2<len(s):   
            if s[p2] not in s[p1:p2]:
                p2+=1
                max_len = max(max_len,p2-p1)
            else:
                while s[p2] in s[p1:p2]:
                    p1+=1
        return max_len
# @lc code=end

