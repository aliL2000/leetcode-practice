from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #MY SOLUTION:
        # I use the permutations library to generate all possible permutations of s1, but as s1 -> n, this get's more labourous, hence this solution is extremely inefficient.
        # if len(s1)>len(s2):
        #     return False
        # perms = set([''.join(p) for p in permutations(s1)])
        # for permutationstring in perms:
        #     if permutationstring in s2:
        #         return True
        # return False

        #ONLINE SOLUTION
        # Use a hashmap to store a key-count pair of the number of characters, then as we go through s2, create a sliding window of current chars
        if len(s1)>len(s2):
            return False
        s1count,s2count = [0]*26,[0]*26
        for i in range(len(s1)):
            s1count[ord(s1[i])- ord('a')] += 1
            s2count[ord(s2[i])- ord('a')] += 1
        matches = 0
        for i in range(26):
            matches += (1 if s1count[i] == s2count[i] else 0)

        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            s2count[index] +=1
            if s1count[index] == s2count[index]:
                matches+=1
            elif s1count[index] + 1 == s2count[index]:
                matches-=1
        
            index = ord(s2[l]) - ord('a')
            s2count[index] +=1
            if s1count[index] == s2count[index]:
                matches+=1
            elif s1count[index] + 1 == s2count[index]:
                matches-=1