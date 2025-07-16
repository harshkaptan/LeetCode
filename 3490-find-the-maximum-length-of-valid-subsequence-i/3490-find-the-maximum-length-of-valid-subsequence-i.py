class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        # dp[i][j]: length of longest valid subsequence where
        # last element mod 2 = i, second‑last mod 2 = j
        dp = [[0, 0], [0, 0]]
        ans = 0
        
        for x in nums:
            r = x & 1  # same as x % 2
            # Try all possible previous mod states j ∈ {0,1}
            for j in (0, 1):
                # Extend a subsequence that ended with y=r and next expected mod is j
                dp[r][j] = dp[j][r] + 1
                ans = max(ans, dp[r][j])
        
        return ans
