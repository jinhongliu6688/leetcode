# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(path, root):
            if not root.left and not root.right:
                result.append(path + [str(root.val)])

            if root.left: 
                dfs(path + [str(root.val)], root.left)
                
            if root.right: 
                dfs(path + [str(root.val)], root.right)
                

        dfs([], root)

        return ["->".join(x) for x in result]
