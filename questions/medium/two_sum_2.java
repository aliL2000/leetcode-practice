//Question can be found here:
//https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
//The only major difference between this and the easy is that the index is only just +1
package questions.medium;

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
                    idx[0] = id+1;
                    idx[1] = i+1;
                    return idx;
                }
            array[i]=nums[i];
        }
        return idx;
    }
}