class Solution:
    def countHillValley(self, nums):
        ans = 0
        n = len(nums)
        prev = 0  # index of the last non-equal value (start at first element)
        for i in range(1, n - 1):
            # Skip plateaus (equal consecutive values)
            if nums[i] == nums[i + 1]:
                continue
            # Hill: nums[i] > both neighbors (closest non-equal neighbors)
            if nums[i] > nums[prev] and nums[i] > nums[i + 1]:
                ans += 1
            # Valley: nums[i] < both neighbors (closest non-equal neighbors)
            if nums[i] < nums[prev] and nums[i] < nums[i + 1]:
                ans += 1
            prev = i
        return ans
