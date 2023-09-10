#Question can be found here:
#https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:

        #MY SOLUTION
        #Really not time efficient whatsoever, if I ever run into a loop, I check to see if it's already there. Should use a set tbh
        # iterations = []
        # iterations.append(n)
        # while(1 not in iterations):
        #     temp_sum = 0
        #     string_number=list(str(n))
        #     for number in string_number:
        #         temp_sum+=int(number)*int(number)
        #     if 1 in iterations:
        #         return True
        #     elif temp_sum in iterations:
        #         return False
        #     else:
        #         iterations.append(temp_sum)
        #         n=temp_sum
        # return True

        #This code below does exactly what I did, but it's far simpler and uses set's to check if the iteration has already happened (loop scenario)
        set_of_no=set()
        while n!=1: 
            #Convert the input number to a string, and using list comprehesion, sum the values of each digit
            n=sum([int(i)**2 for i in str(n)])
            #Check to see if it's in the set, and if it is, return False, else return True after reaching 1
            if n in set_of_no:
                return False 
            set_of_no.add(n) 
        return True
    
