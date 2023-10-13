# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(path, root):
            if not root.left and not root.right:
                return sum(path + [root.val]) == targetSum

            if root.left and root.right:
                return dfs(path + [root.val], root.left) or dfs(path + [root.val], root.right)
            elif root.left:
                return dfs(path + [root.val], root.left)
            elif root.right:
                return dfs(path + [root.val], root.right)

        return dfs([], root)
