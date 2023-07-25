#Question can be found here:
#https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:

        res = 0
        l,r = 0,len(height)-1
        while l<r:
            area = (r-l)*min(height[l],height[r])
            res = max(area,res)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            
        return res
        # l,r = 0,len(height)-1
        # while l<r:
        #     print("--")
        #     area = (r-l)*min(height[l],height[r])
        #     print(area,l,r)
        #     if (r-(l+1))*min(height[l+1],height[r]) > area:
        #         print("a", (r-l+1),min(height[l+1],height[r]), area)
        #         l += 1
        #     elif (r-l-1)*min(height[l],height[r-1]) > area:
        #         print("b")
        #         r -= 1
            
        #     if (r-l) * max(height) <= area:
        #         break 
        # return area