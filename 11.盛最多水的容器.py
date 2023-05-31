#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        res = 0
        while l<r:
            res = max(res, (r-l)*min(height[l],height[r]))
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return res
# @lc code=end

