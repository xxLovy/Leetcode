[94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

recursive

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = [] 
        if not root:
            return ret
        ret.extend(self.inorderTraversal(root.left))
        ret.append(root.val)
        ret.extend(self.inorderTraversal(root.right))
        return ret
        
```

[144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

recursive

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = [] 
        if not root:
            return ret
        ret.append(root.val)
        ret.extend(self.preorderTraversal(root.left))
        ret.extend(self.preorderTraversal(root.right))
        return ret
```

[145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

recursive

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = [] 
        if not root:
            return ret
        ret.extend(self.postorderTraversal(root.left))
        ret.extend(self.postorderTraversal(root.right))
        ret.append(root.val)
        return ret
```

