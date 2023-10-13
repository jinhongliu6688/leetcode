# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        result = []

        def dfs(path, root):
            if not root.left and not root.right and sum(path + [root.val]) == targetSum:
                result.append(path + [root.val])
                return
            
            if root.left: dfs(path + [root.val], root.left)
            if root.right: dfs(path + [root.val], root.right)

        dfs([], root)

        return result
