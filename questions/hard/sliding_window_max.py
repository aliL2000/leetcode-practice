

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #My naive solution, the issue is runtime, i am constantly creating a new sublist and re-setting the max list, not efficient whatso-ever
        res = []
        for i in range(len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res