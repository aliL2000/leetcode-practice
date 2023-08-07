//Question can be found here:
//https://leetcode.com/problems/two-sum/
package questions.easy;

import java.util.Arrays;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Integer[] array = new Integer[nums.length];
        int[] idx = new int[2];
        for(int i=0;i<nums.length;i++){
            int needed = target - nums[i];
            if(Arrays.asList(array).contains(needed))
                {
                    int id = Arrays.asList(array).indexOf(needed);
                    idx[0] = id;
                    idx[1] = i;
                    return idx;
                }
            array[i]=nums[i];
        }
        return idx;


        /*
         * This solution is not mine, but it's extremely fast even though it has two for loops?
         *      
        int[] ans=new int[2];
        for(int i=1;i<nums.length;i++){
            for(int j=i;j<nums.length;j++){
                if(nums[j-i]+nums[j]==target){
                    ans[0]=j-i;
                    ans[1]=j;
                    return ans;
                }
            }
        }
        return ans;
         */
    }
}