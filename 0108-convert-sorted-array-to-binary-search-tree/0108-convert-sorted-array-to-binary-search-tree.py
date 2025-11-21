# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        # Initialize root
        n = len(nums)
        left, right = 0, n - 1
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        
        # Stack stores: (current_node, left_index, right_index)
        stack = [(root, left, right)]
        
        while stack:
            node, l, r = stack.pop()
            mid = (l + r) // 2
            
            # Process Left Child
            # If there are elements to the left of mid
            if l <= mid - 1:
                left_mid = (l + mid - 1) // 2
                node.left = TreeNode(nums[left_mid])
                stack.append((node.left, l, mid - 1))
            
            # Process Right Child
            # If there are elements to the right of mid
            if mid + 1 <= r:
                right_mid = (mid + 1 + r) // 2
                node.right = TreeNode(nums[right_mid])
                stack.append((node.right, mid + 1, r))
                
        return root