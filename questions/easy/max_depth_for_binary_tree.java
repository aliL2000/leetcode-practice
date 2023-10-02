

class Solution {
    public int maxDepth(TreeNode root) {
        System.out.println(root);
        if (root == null){
            return 0;
        }
        int cap = 0;
        return depth(cap, root);
    }
    public int depth(int length, TreeNode root) {
         if (root == null){
             return length;
         }
         else{
             return Math.max(depth(length+1,root.left),depth(length+1,root.right));
         }
    }
}
