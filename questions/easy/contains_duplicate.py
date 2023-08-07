#Question can be found here:
#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Set holds ONLY unique values, so create a set from the given nums list, and check to see if they're equivalent in length (hence no duplicates and return false)
        #This is my solution, not really the most time or space efficient
        #MY SOLUTION
        #return len(nums)!=len(set(nums))
        
        
        #This solution below is 90% faster than other ones
        #It creates a set, then iteratively adds each number to the set, and checks for duplicates, I'm therefore assuming using the set constructor with a given list is the slow part of my above solution
        #FASTER SOLUTION
        seen = set()  # Create an empty set to store seen elements
        for num in nums:
            if num in seen:
                return True  # Duplicate found
            seen.add(num)  # Add the current element to the set
        return False