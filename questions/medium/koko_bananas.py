#Question can be found here:
#https://leetcode.com/problems/koko-eating-bananas/

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        returned = r
        while l<=r:
            k=(l+r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours<=h:
                returned = min(returned,k)
                r = k-1
            else:
                l = k+1

        return returned