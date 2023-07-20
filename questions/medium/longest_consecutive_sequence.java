//Question can be found here:
//https://leetcode.com/problems/longest-consecutive-sequence/

package questions.medium;
import java.util.Arrays;

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0)
            return 0;
        Arrays.sort(nums);
        int overall_max = 0;
        int current_max = 0;
        for (int i = 0; i< nums.length-1;i++){
            if (nums[i] + 1 == nums[i+1] || nums[i] == nums[i+1]){
                if (nums[i] != nums[i+1])
                    current_max=current_max+1;
                if (current_max>overall_max)
                    overall_max=current_max;
            }
            else{
                current_max=0;
            }
        }
        return overall_max+1;
    }
}