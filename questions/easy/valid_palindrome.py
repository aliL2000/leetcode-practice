import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        return filtered_string == filtered_string[::-1]