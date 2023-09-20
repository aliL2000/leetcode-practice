#Question can be found here:
#

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #My naive solution, the issue is runtime, i am constantly creating a new sublist and re-setting the max list, not efficient whatso-ever
        #Runtime is O(k(n-k)), which is terribly inefficient
        # res = []
        # for i in range(len(nums)-k+1):
        #     res.append(max(nums[i:i+k]))
        # return res

        #Non-original solution
        #Uses a queue and adds and removes the max values for each window as we iterate through nums
        res = []
        l,r = 0,0
        q = collections.deque()
        while r<len(nums):
            #pop smaller values from the q, making it emptier
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #remove left val
            if l>q[0]:
                q.popleft()
            if (r+1)>=k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res