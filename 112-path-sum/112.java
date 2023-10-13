/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
       if (root == null) {
           return false;
       }

       return dfs(0, root, targetSum);
    }
    
    private boolean dfs(int cur_sum, TreeNode root, int targetSum) {
        if (root.left == null && root.right == null) {
            return cur_sum + root.val == targetSum;
        }

        if (root.left != null && root.right != null) {
            return dfs(cur_sum + root.val, root.left, targetSum) || dfs(cur_sum + root.val, root.right, targetSum);
        } else if(root.left != null) {
            return dfs(cur_sum + root.val, root.left, targetSum);
        } else if (root.right != null) {
            return dfs(cur_sum + root.val, root.right, targetSum);
        }

        return false;
    }
}
