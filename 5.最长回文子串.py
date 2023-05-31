#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def helper(s, i, j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        
        res = ""
        for i in range(len(s)):
            # 奇数
            tmp1 = helper(s, i, i)
            tmp2 = helper(s, i, i + 1)
            res = max(res, tmp1, tmp2, key=len)
        return res
# @lc code=end

