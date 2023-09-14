class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        l,r = 0,1
        maxlength = 1
        current_string = s[0]
        while r < len(s):
            if s[r] not in current_string:
                current_string += s[r]
                maxlength = max(len(current_string),maxlength)
            else:
                l+=1
                r = l
                current_string = s[l]
            r+=1
        return maxlength
        