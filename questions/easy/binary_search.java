//Question can be found here:
//https://leetcode.com/problems/binary-search

package questions.easy;

class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int index = (left + right) / 2;
            if (nums[index] < target) {
                left = index + 1;
            } else if (nums[index] > target) {
                right = index - 1;
            } else {
                return index;
            }
        }
        return -1;
    }
}