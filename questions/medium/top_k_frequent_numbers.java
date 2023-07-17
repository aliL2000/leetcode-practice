//Question can be found here:
//https://leetcode.com/problems/top-k-frequent-elements/

package questions.medium;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        //Use a Datastructure to store key-value pairs
        HashMap<Integer, Integer> countNumbers = new HashMap<Integer, Integer>();
        for(int i=0;i<nums.length;i++){
            if (countNumbers.containsKey(nums[i])){
                countNumbers.put(nums[i], countNumbers.get(nums[i])+1);
            }
            else {
                countNumbers.put(nums[i], 1);
            }
        }
        //Output top K values and sort by desc value
        int[] output = new int[k];
        int j = 0;
        for(int i = 0 ; i< k ;i++){
            int freq = 0;
            int max = 0;
            for(Map.Entry<Integer,Integer> val : countNumbers.entrySet()){
                if(val.getValue() > freq){
                   freq = val.getValue();
                   max = val.getKey();
                }
            }
            countNumbers.put(max,0);
            output[j] = max;
            j++;
        }
       return output;
    }
}