import heapq

class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        """
        Calculates the minimum possible difference between the sums of two parts of an array.

        The problem asks to remove a subsequence of n elements from an array of 3*n elements.
        The remaining 2*n elements are split into two equal halves. The goal is to minimize
        the difference between the sum of the first half and the sum of the second half.

        This can be rephrased as finding a partition point `i` (from n to 2n) in the original
        array, such that we choose the n smallest elements from the prefix `nums[0...i-1]`
        and the n largest elements from the suffix `nums[i...3n-1]`. The removed elements are
        the `i-n` largest from the prefix and the `(3n-i)-n` smallest from the suffix.

        The algorithm works as follows:
        1.  Calculate `prefix_min_sum`: `prefix_min_sum[i]` will store the minimum possible
            sum of n elements in the subarray `nums[0...i]`. This is achieved by iterating
            from left to right, maintaining a max-heap of size n to keep track of the n
            smallest elements seen so far.

        2.  Calculate `suffix_max_sum`: `suffix_max_sum[i]` will store the maximum possible
            sum of n elements in the subarray `nums[i...3n-1]`. This is done by iterating
            from right to left, using a min-heap of size n to keep track of the n largest
            elements.

        3.  Find the minimum difference: Iterate through all possible split points `i` from
            n to 2n (inclusive). For each split point, the first part is chosen from `nums[0...i-1]`
            and the second part from `nums[i...3n-1]`. The minimum difference will be the
            minimum of `prefix_min_sum[i-1] - suffix_max_sum[i]` over all valid `i`.
        """
        n = len(nums) // 3
        
        # Calculate prefix sums of the n smallest elements
        prefix_min_sum = [0] * (3 * n)
        max_heap = []
        current_sum = 0
        for i in range(2 * n):
            heapq.heappush(max_heap, -nums[i])
            current_sum += nums[i]
            if len(max_heap) > n:
                current_sum += heapq.heappop(max_heap)
            if len(max_heap) == n:
                prefix_min_sum[i] = current_sum

        # Calculate suffix sums of the n largest elements
        suffix_max_sum = [0] * (3 * n)
        min_heap = []
        current_sum = 0
        for i in range(3 * n - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            current_sum += nums[i]
            if len(min_heap) > n:
                current_sum -= heapq.heappop(min_heap)
            if len(min_heap) == n:
                suffix_max_sum[i] = current_sum
                
        # Find the minimum difference
        min_diff = float('inf')
        for i in range(n - 1, 2 * n):
            min_diff = min(min_diff, prefix_min_sum[i] - suffix_max_sum[i + 1])
            
        return min_diff