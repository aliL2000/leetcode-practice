import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        return filtered_string == filtered_string[::-1]
        #alternative solution using two pointers on the string
        # string_length = len(filtered_string)
        # for i in range(int(string_length/2)):
        #     if filtered_string[i]!=filtered_string[string_length-i-1]:
        #         return False
        # return True