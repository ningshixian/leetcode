#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l1, l2 = len(s)+1, len(p)+1
        dp = [[False]*(l2) for _ in range(l1)]
        
        dp[0][0] = True
        for k in range(1, l2):
            if p[k-1]=='*':
                dp[0][k] = dp[0][k-2]
        
        for i in range(1, l1):
            for j in range(1, l2):
                if s[i-1]==p[j-1] or p[j-1]=='.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=='*':
                    if s[i-1]==p[j-2] or p[j-2]=='.':
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2]
        
        return dp[l1-1][l2-1]

# @lc code=end

