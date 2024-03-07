[112. Path Sum](https://leetcode.com/problems/path-sum/)

Backtracking

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # backtracking
        if not root:
            return False
        
        # leafnode
        if not root.right and not root.left:
            return True if targetSum == root.val else False
        left = right = False
        if root.left:
            left = self.hasPathSum(root.left, targetSum-root.val)
        if root.right:
            right = self.hasPathSum(root.right, targetSum-root.val)

        return left or right
        
        
        
```

