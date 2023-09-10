#Question can be found here:
#https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        #MY SOLUTION
        #Not efficient, I am using list comprehension, and casting each character to an str, then re-casting to an int plus 1
        #Then, I return a list where I've casted each individual digit to a character, then back to an int
        # b=int("".join(str(c) for c in digits))+1
        # return [int(x) for x in str(b)]

        #Online solution that uses the map function to map each digit to a string, then joins those strings and cast to an int
        #Perhaps the map function is far quicker than list comprehension
        num = int(''.join(map(str,digits))) + 1
        nums = [int(i) for i in str(num)]
        return nums