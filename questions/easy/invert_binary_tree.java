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
    public TreeNode invertTree(TreeNode root) {
        if (root==null){
            return null;
        }
         //Swap the root's left and right child nodes
        TreeNode tmp = root.left;
        root.left = root.right;
        root.right = tmp;
        //Then recursively call the same swapper method on those child nodes (This will continue until we reach the bottom of the BT)
        invertTree(root.left);
        invertTree(root.right);
        return root;
    }
}