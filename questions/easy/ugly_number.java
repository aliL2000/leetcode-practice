//Question can be found here:
//https://leetcode.com/problems/ugly-number/

package questions.easy;

class Solution {
    public boolean isUgly(int n) {
        if (n==0) return false;
        int[] primes = {2,3,5};
        for(int i=0;i<primes.length;i++){
            while (n%primes[i] == 0){
                n=n/primes[i];
            }
            if (n == 1)
                return true;
        }
        return false;
    } 
}
