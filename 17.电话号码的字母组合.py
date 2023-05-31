#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        tmp = []
        height = len(digits)
        
        def dfs(digits2, h, path): 
            if h==height:
                tmp.append("".join(path))
                return 

            for i in d[digits2[0]]:
                path.append(i)
                dfs(digits2[1:], h+1, path)
                path.pop()
            
            return tmp
        
        if not digits:
            return tmp

        dfs(digits, 0, [])
        return tmp
# @lc code=end

