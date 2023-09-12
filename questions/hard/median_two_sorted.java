package questions.hard;
import java.util.Arrays;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] newList = new int[nums1.length + nums2.length];
        System.arraycopy(nums1, 0, newList, 0, nums1.length);
        System.arraycopy(nums2, 0, newList, nums1.length, nums2.length);
        Arrays.sort(newList);
        int l = 0, r = newList.length;
        if (r%2==0)
            return (newList[l+r/2] + newList[l+r/2-1]) / (double) 2;
        else
            return newList[l+r/2];
    }
}