#Question can be found here:
#https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        iterations = []
        iterations.append(n)
        while(1 not in iterations):
            temp_sum = 0
            string_number=list(str(n))
            for number in string_number:
                temp_sum+=int(number)*int(number)
            if 1 in iterations:
                return True
            elif temp_sum in iterations:
                return False
            else:
                iterations.append(temp_sum)
                n=temp_sum
        return True