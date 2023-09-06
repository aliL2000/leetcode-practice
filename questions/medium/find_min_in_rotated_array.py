class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        currentmin = nums[0]
        rotatedvalue = nums[-1]
        while(currentmin>rotatedvalue):
            popped = nums.pop(length-1)
            nums.insert(0,popped)
            currentmin = popped
            rotatedvalue = nums[-1]
        return nums[0]
