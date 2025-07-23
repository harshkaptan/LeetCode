class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        seen = set()
        left = 0
        curr_sum = 0
        max_sum = 0
        for right, num in enumerate(nums):
            while num in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            seen.add(num)
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
        return max_sum
