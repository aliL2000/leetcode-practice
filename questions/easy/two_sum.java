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
    }
}