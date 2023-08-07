//Question can be found here:
//https://leetcode.com/problems/product-of-array-except-self/

package questions.medium;
import java.util.Arrays;

class Solution {

    // This solution runs in 2ms, and the most efficient solution is not too different, so this is the only solution provided.
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        Arrays.fill(res, 1);
        int prefix = 1;
        for(int i = 0; i < nums.length; i++){
            res[i] = prefix;
            prefix *= nums[i];
        }
        int postfix = 1;
        for(int i = nums.length -1; i>-1;i--){
            res[i] *= postfix;
            postfix *= nums[i];
        }
        return res;
    }
}