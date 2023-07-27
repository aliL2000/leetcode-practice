#Question can be found here:
#https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x * x, n // 2)
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res

        #My solution below, it works fine, but it's too slow, this solution above uses more memory, but is faster
        # xreturned = x
        # for i in range(abs(n)-1):
        #     xreturned = xreturned * x
        # print(xreturned)
        # return xreturned if n >= 0 else 1 / xreturned