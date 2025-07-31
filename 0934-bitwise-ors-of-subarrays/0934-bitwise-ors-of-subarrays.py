class Solution:
    def subarrayBitwiseORs(self, arr):
        res = set()
        cur = set()
        for num in arr:
            # For each num, new set is OR with all of last step and num itself
            cur = {num | x for x in cur} | {num}
            res |= cur
        return len(res)
