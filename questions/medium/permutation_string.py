from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #MY SOLUTION:
        # I use the permutations library to generate all possible permutations of s1, but as s1 -> n, this get's more labourous, hence this solution is extremely inefficient.
        if len(s1)>len(s2):
            return False
        perms = set([''.join(p) for p in permutations(s1)])
        for permutationstring in perms:
            if permutationstring in s2:
                return True
        return False