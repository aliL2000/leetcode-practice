#Question can be found here:
#https://leetcode.com/problems/group-anagrams/
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for str in strs:
            count = [0] * 26;
            for character in str:
                count[ord(character)-ord("a")] += 1
            res[tuple(count)].append(str)
        return res.values()