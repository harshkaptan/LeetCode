from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        last = [0] * 32   # For each bit position, store the **rightmost** index where we saw it

        for i in range(n - 1, -1, -1):
            for bit in range(32):
                if nums[i] & (1 << bit):
                    last[bit] = i
            furthest = i
            for bit in range(32):
                if last[bit]:
                    furthest = max(furthest, last[bit])
            res[i] = furthest - i + 1
        return res
