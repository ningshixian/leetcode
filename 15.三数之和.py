#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def twosum(nums, j, target):
            nums = nums[j+1:]
            l,r = 0, len(nums)-1
            while l<r:
                if nums[l]+nums[r]==target:
                    return [-target, nums[l], nums[r]]
                elif nums[l]+nums[r]>target:
                    r-=1
                else:
                    l+=1
        
        prev = None
        res = []
        for i in enumerate(nums):
            if nums[i]==prev: continue
            if nums[i]>0: break
            target = -nums[i]
            _ = twosum(nums, i, target)
            if _:
                res.append(_)
        
        return res
# @lc code=end

