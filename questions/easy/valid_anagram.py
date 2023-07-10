#Question can be found here:
#https://leetcode.com/problems/valid-anagram/
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Provdided two solutions, one uses the counter library given in Python, and one uses Python lists
        #First solution is better runtime and memory usage

        #First Solution:
        one = Counter(s)
        two = Counter(t)
        return one==two

        #Second Solution
        # if (len(s)!=len(t)):
        #     return False
        # firstlist = list(s)
        # secondlist = list(t)
        # firstlist.sort()
        # secondlist.sort()
        # for i in range(len(firstlist)):
        #     if firstlist[i]!=secondlist[i]:
        #         return False
        # return True