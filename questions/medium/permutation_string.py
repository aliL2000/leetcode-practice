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
        # if len(s1)>len(s2):
        #     return False
        # s1Count,s2Count = [0]*26,[0]*26
        # for i in range(len(s1)):
        #     s1Count[ord(s1[i])- ord('a')] += 1
        #     s2Count[ord(s2[i])- ord('a')] += 1
        
        # matches = sum(map(lambda i: s1Count[i] == s2Count[i], range(26)))

        # for l in range(len(s2) - len(s1)):
        #     if matches == 26:
        #         return True

        #     i = ord(s2[l]) - ord("a")
        #     s2Count[i] -= 1
        #     if s2Count[i] == s1Count[i]:
        #         matches += 1
        #     elif s2Count[i] == s1Count[i] - 1:
        #         matches -= 1

        #     i = ord(s2[l + len(s1)]) - ord("a")
        #     s2Count[i] += 1
        #     if s2Count[i] == s1Count[i]:
        #         matches += 1
        #     elif s2Count[i] == s1Count[i] + 1:
        #         matches -= 1

        # return matches == 26
    
        #OPTMIZED SOLUTION 
                
        if len(s1) > len(s2): return False
        
        
        # Use sliding window technique
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        window_len = len(s1)
        
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
    
        for j in range(window_len, len(s2)):
            if s1_count == s2_count: return True
            
            s2_count[ord(s2[j-window_len]) - ord('a')] -= 1
            s2_count[ord(s2[j]) - ord('a')] += 1
        return s1_count == s2_count   