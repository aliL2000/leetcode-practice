#Question can be found here:
#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Set holds ONLY unique values, so create a set from the given nums list, and check to see if they're equivalent in length (hence no duplicates and return false)
        return len(nums)!=len(set(nums))