#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = (1 + dp[i-1][j-1]
                            if text1[i - 1] == text2[j-1]
                            else max(dp[i][j-1], dp[i-1][j]))

        return dp[-1][-1]

# @lc code=end
