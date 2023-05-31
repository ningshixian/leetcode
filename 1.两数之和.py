#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {a:i for i,a in enumerate(nums)}
        for j in range(len(nums)):
            if target-nums[j] in d and d[target-nums[j]] != j:
                return [j,d[target-nums[j]]]
# @lc code=end

